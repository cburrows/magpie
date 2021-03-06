# This is used by GYP to generate platform-specific project files for building
# Magpie. (I.e. on a Mac it will create an XCode project, on Linux a makefile.)
# See README for more.

{
  'xcode_settings': {
    'GCC_ENABLE_CPP_EXCEPTIONS': 'NO', # -fno-exceptions
    'GCC_ENABLE_CPP_RTTI': 'NO', # -fno-rtti
    'GCC_TREAT_WARNINGS_AS_ERRORS': 'YES',    # -Werror
    'GCC_WARN_CHECK_SWITCH_STATEMENTS': 'YES', # -Wswitch
    'WARNING_CFLAGS': [
      '-Wall',
      '-W',
      '-Wno-unused-parameter',
      '-Wnon-virtual-dtor',
    ],
  },
  'configurations': {
    'Debug': {
      'cflags': [ '-g', '-O0' ],
      'defines': [ 'DEBUG' ],
      'xcode_settings': {
        'GCC_OPTIMIZATION_LEVEL': '0',
      },
    },
    'Release': {
      'cflags': [ '-O3' ],
      'xcode_settings': {
        'GCC_OPTIMIZATION_LEVEL': '3',
      },
    },
  },
  'target_defaults': {
    'default_configuration': 'Debug',
    'configurations': {
      'Debug': {
      },
      'Release': {
      },
    },
    'include_dirs': [
      'src/Base',
      'src/Compiler',
      'src/Memory',
      'src/Syntax',
      'src/VM',
    ],
    'sources': [
      'src/Base/Array.h',
      'src/Base/Macros.h',
      'src/Base/MagpieString.cpp',
      'src/Base/MagpieString.h',
      'src/Base/Queue.h',
      'src/Base/Stack.h',
      'src/Compiler/Bytecode.h',
      'src/Compiler/Compiler.cpp',
      'src/Compiler/Compiler.h',
      'src/Memory/ForwardingAddress.h',
      'src/Memory/Managed.cpp',
      'src/Memory/Managed.h',
      'src/Memory/Memory.cpp',
      'src/Memory/Memory.h',
      'src/Memory/RootSource.h',
      'src/Memory/Semispace.cpp',
      'src/Memory/Semispace.h',
      'src/Syntax/Lexer.cpp',
      'src/Syntax/Lexer.h',
      'src/Syntax/Node.cpp',
      'src/Syntax/Node.h',
      'src/Syntax/NodeVisitor.h',
      'src/Syntax/Parser.cpp',
      'src/Syntax/Parser.h',
      'src/Syntax/Token.cpp',
      'src/Syntax/Token.h',
      'src/VM/Fiber.cpp',
      'src/VM/Fiber.h',
      'src/magpie.1',
      'src/VM/Method.cpp',
      'src/VM/Method.h',
      'src/VM/Object.cpp',
      'src/VM/Object.h',
      'src/VM/VM.cpp',
      'src/VM/VM.h',
    ],
  },
  'targets': [
    {
      'target_name': 'magpie',
      'type': 'executable',
      'sources': [
        'src/main.cpp',
      ],
    },
    {
      'target_name': 'unit_tests',
      'type': 'executable',
      'defines': [ 'UNIT_TEST' ],
      'include_dirs': [
        'src/Test',
      ],
      'sources': [
      'src/Test/LexerTests.cpp',
      'src/Test/LexerTests.h',
      'src/Test/MemoryTests.cpp',
      'src/Test/MemoryTests.h',
      'src/Test/ParserTests.cpp',
      'src/Test/ParserTests.h',
      'src/Test/QueueTests.cpp',
      'src/Test/QueueTests.h',
      'src/Test/StringTests.cpp',
      'src/Test/StringTests.h',
      'src/Test/Test.cpp',
      'src/Test/Test.h',
      'src/Test/TestMain.cpp',
      'src/Test/TokenTests.cpp',
      'src/Test/TokenTests.h',
      ],
    },
  ],
}
