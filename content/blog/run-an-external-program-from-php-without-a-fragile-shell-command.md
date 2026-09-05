+++
title = "Run an External Program from PHP Without a Fragile Shell Command"
slug = "run-an-external-program-from-php-without-a-fragile-shell-command"
date = "2012-03-02T00:32:57+01:00"
lastmod = "2026-09-05T00:00:00+00:00"
draft = false
description = "A practical way to run an external program from PHP with fixed executables, argument arrays, timeouts, limited permissions, and checked failures."
summary = "PHP can start another program, but joining input into a shell command creates avoidable risk. I prefer argument arrays and explicit operating limits."
tags = ["PHP", "Symfony Process", "security", "subprocesses", "backend development", "reliability"]
priority = true
priority_topics = ["tech"]
original_title = "Exécuter un programme distant via PHP"
source_01script = "https://01script.com/execute-programme-avec-php/"
+++

My original article used PHP's `exec()` function to start a Perl script and print its output. The example explained the function's output and return-code arguments, but it did not define a security boundary or handle failures.

Starting another program is sometimes the right solution. Building a command string from request data is not.

## I First Check Whether I Need a Process

I prefer a library or service API when one exists. It gives me typed inputs, structured errors, and fewer operating-system differences.

An external process still makes sense when I need a mature command-line tool, an existing worker, or a program written in another language. In that case, I treat the executable as part of my application's trusted configuration. A visitor never chooses which binary is run.

## I Pass Arguments as an Array

For a Composer project, the [Symfony Process component](https://symfony.com/doc/current/components/process.html) provides a clear interface around process execution:

```bash
composer require symfony/process
```

Here is a complete command-line example. It requires PHP CLI and Composer. In the project directory, `run.php` contains:

```php
<?php

use Symfony\Component\Process\Exception\ProcessTimedOutException;
use Symfony\Component\Process\Exception\RuntimeException as ProcessRuntimeException;
use Symfony\Component\Process\Process;

require __DIR__ . '/vendor/autoload.php';

if (PHP_SAPI !== 'cli') {
    exit('Run this example from the command line.');
}

$mode = $argv[1] ?? 'preview';
$allowedModes = ['preview', 'export'];

if (!in_array($mode, $allowedModes, true)) {
    fwrite(STDERR, "Unsupported mode.\n");
    exit(2);
}

$phpBinary = PHP_BINARY;

$process = new Process([
    $phpBinary,
    __DIR__ . '/worker.php',
    '--mode',
    $mode,
], __DIR__);
$process->setTimeout(30);

try {
    $process->mustRun();
    echo $process->getOutput();
} catch (ProcessTimedOutException $exception) {
    fwrite(STDERR, "The worker exceeded its time limit.\n");
    exit(1);
} catch (ProcessRuntimeException $exception) {
    fwrite(STDERR, "The worker could not complete.\n");
    exit(1);
}
```

Alongside it, `worker.php` contains a small demonstration that prints the accepted mode. It does not export any data:

```php
<?php

$options = getopt('', ['mode:']);
$mode = $options['mode'] ?? '';

if (!in_array($mode, ['preview', 'export'], true)) {
    fwrite(STDERR, "Unsupported mode.\n");
    exit(2);
}

echo "Mode: {$mode}\n";
```

Running `php run.php preview` prints `Mode: preview`. An unsupported argument exits before starting the worker. A worker failure and a timeout produce separate, short error messages.

The executable and each argument are separate array elements. `PHP_BINARY` works here because the parent is explicitly a CLI script. In a web application, I configure and verify a PHP CLI executable separately. Argument arrays do not replace input validation or restrict what the chosen program can do.

This demonstration has a fixed, small output. A timeout alone does not limit output size, and Symfony inherits the parent's environment by default. Before using a different worker, I review its output volume, inherited secrets, and permissions. The checks below describe that additional work.

## Native PHP Can Also Avoid a Command String

When adding a dependency is not justified, [`proc_open()`](https://www.php.net/manual/en/function.proc-open.php) accepts the command as an array on PHP 7.4 and later. PHP can then start the process directly and manage its arguments without passing a command string through a shell.

`proc_open()` also exposes standard input, standard output, and standard error through descriptors. That control is useful, but it creates more code to close pipes, collect output, and release the process correctly. I use it when I need that control and test every exit path.

The older [`exec()`](https://www.php.net/manual/en/function.exec.php) function still returns the last output line and can populate an output array and result code. It accepts only a command string, so any variable argument requires careful shell handling. I avoid it when an argument-array API can do the job.

## I Define the Operating Limits

The code that starts a process is only one part of the design. I also define:

- a fixed executable or a short allowlist;
- validated argument values;
- a dedicated working directory;
- the minimum environment variables needed;
- a timeout and output-size limit;
- permissions that do not exceed the task;
- separate handling for standard output, standard error, and the exit code;
- logs that do not expose secrets or personal data.

I never run the web application as root. I also avoid starting a long task inside an HTTP request. Work that can outlive the request belongs in a queue with retry rules, duplicate protection, and a visible result.

## I Test Failure, Not Only Output

My original example proved that PHP could print the lines returned by a Perl script. A production test must also cover an unknown mode, a missing executable, a non-zero exit code, a timeout, large output, and a process that writes only to standard error.

The useful idea remains the same: PHP can coordinate an existing program. The current version adds the boundary that the first article lacked. The application chooses the program, validates each argument, limits execution, and treats every failure as data to handle.
