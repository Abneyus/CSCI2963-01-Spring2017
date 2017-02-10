**** STEP01 ****
```
bears:build/ (master) $ cmake ../step01                                                                            [11:45:53]
-- The C compiler identification is GNU 4.8.4
-- The CXX compiler identification is GNU 4.8.4
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Configuring done
-- Generating done
-- Build files have been written to: /mnt/c/Users/Elijah/Dropbox/Intro-to-Open-Source/CSCI2963-01-Spring2017/lab04/build
bears:build/ (master✗) $ make                                                                                      [11:46:07]
Scanning dependencies of target Tutorial
[100%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
Linking CXX executable Tutorial
[100%] Built target Tutorial
bears:build/ (master✗) $ ./Tutorial 169                                                                            [11:46:12]
The square root of 169 is 13
bears:build/ (master✗) $                                                                                           [11:46:19]
```
**** STEP02 ****
```
bears:build/ (master✗) $ cmake ../step02                                                                           [11:50:56]
-- Configuring done
-- Generating done
-- Build files have been written to: /mnt/c/Users/Elijah/Dropbox/Intro-to-Open-Source/CSCI2963-01-Spring2017/lab04/build
bears:build/ (master✗) $ make                                                                                      [11:50:58]
Scanning dependencies of target MathFunctions
[ 50%] Building CXX object MathFunctions/CMakeFiles/MathFunctions.dir/mysqrt.cxx.o
Linking CXX static library libMathFunctions.a
[ 50%] Built target MathFunctions
Scanning dependencies of target Tutorial
[100%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
Linking CXX executable Tutorial
[100%] Built target Tutorial
bears:build/ (master✗) $ ./Tutorial 169                                                                            [11:51:03]
Computing sqrt of 169 to be 85
Computing sqrt of 169 to be 43.4941
Computing sqrt of 169 to be 23.6899
Computing sqrt of 169 to be 15.4119
Computing sqrt of 169 to be 13.1887
Computing sqrt of 169 to be 13.0014
Computing sqrt of 169 to be 13
Computing sqrt of 169 to be 13
Computing sqrt of 169 to be 13
Computing sqrt of 169 to be 13
The square root of 169 is 13
bears:build/ (master✗) $                                                                                           [11:51:11]
```
**** STEP03 ****
```
bears:build/ (master✗) $ cmake ../step03                                                                           [11:52:05]
-- The C compiler identification is GNU 4.8.4
-- The CXX compiler identification is GNU 4.8.4
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Configuring done
-- Generating done
-- Build files have been written to: /mnt/c/Users/Elijah/Dropbox/Intro-to-Open-Source/CSCI2963-01-Spring2017/lab04/build
bears:build/ (master✗) $ make                                                                                      [11:52:16]
Scanning dependencies of target Tutorial
[100%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
Linking CXX executable Tutorial
[100%] Built target Tutorial
bears:build/ (master✗) $ ctest                                                                                     [11:52:23]
Test project /mnt/c/Users/Elijah/Dropbox/Intro-to-Open-Source/CSCI2963-01-Spring2017/lab04/build
    Start 1: TutorialRuns
1/5 Test #1: TutorialRuns .....................   Passed    0.03 sec
    Start 2: TutorialComp25
2/5 Test #2: TutorialComp25 ...................   Passed    0.04 sec
    Start 3: TutorialNegative
3/5 Test #3: TutorialNegative .................Failed  Required regular expression not found.Regex=[-25 is 0
]  0.04 sec
    Start 4: TutorialSmall
4/5 Test #4: TutorialSmall ....................   Passed    0.04 sec
    Start 5: TutorialUsage
5/5 Test #5: TutorialUsage ....................   Passed    0.04 sec

80% tests passed, 1 tests failed out of 5

Total Test time (real) =   0.23 sec

The following tests FAILED:
          3 - TutorialNegative (Failed)
Errors while running CTest
bears:build/ (master✗) $                                                                                           [11:52:27]

```
**** TEST04 ****
```
bears:build/ (master✗) $ cmake ../step04                                                                           [11:53:24]
-- The C compiler identification is GNU 4.8.4
-- The CXX compiler identification is GNU 4.8.4
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Looking for log
-- Looking for log - not found
-- Looking for exp
-- Looking for exp - not found
-- Configuring done
-- Generating done
-- Build files have been written to: /mnt/c/Users/Elijah/Dropbox/Intro-to-Open-Source/CSCI2963-01-Spring2017/lab04/build
bears:build/ (master✗) $ make                                                                                      [11:53:38]
Scanning dependencies of target Tutorial
[100%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
Linking CXX executable Tutorial
[100%] Built target Tutorial
bears:build/ (master✗) $ ./Tutorial 169                                                                            [11:53:43]
The square root of 169 is 13
bears:build/ (master✗) $                                                                                           [11:53:46]
```
**** STEP05 ****
```
bears:build/ (master✗) $ cmake ../step05                                                                           [11:56:23]
-- The C compiler identification is GNU 4.8.4
-- The CXX compiler identification is GNU 4.8.4
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Looking for log
-- Looking for log - not found
-- Looking for exp
-- Looking for exp - not found
-- Configuring done
-- Generating done
-- Build files have been written to: /mnt/c/Users/Elijah/Dropbox/Intro-to-Open-Source/CSCI2963-01-Spring2017/lab04/build
bears:build/ (master✗) $ make                                                                                      [11:56:31]
Scanning dependencies of target Tutorial
[100%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
Linking CXX executable Tutorial
[100%] Built target Tutorial
bears:build/ (master✗) $ ./Tutorial 169                                                                            [11:56:34]
The square root of 169 is 13
bears:build/ (master✗) $                                                                                           [11:56:37]
```
