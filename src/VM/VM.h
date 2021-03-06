#pragma once

#include "Fiber.h"
#include "Lexer.h"
#include "Macros.h"
#include "Memory.h"
#include "Method.h"
#include "RootSource.h"

namespace magpie
{
  // The main Virtual Machine class for a running Magpie interpreter.
  class VM : public RootSource
  {
  public:
    VM();

    virtual void reachRoots();

    Fiber& fiber() { return *fiber_; }

    MethodScope& globals() { return globals_; }
    
    inline gc<Object> getBool(bool value) const
    {
      return value ? true_ : false_;
    }
    
  private:
    MethodScope globals_;
    gc<Fiber> fiber_;
    
    gc<Object> true_;
    gc<Object> false_;

    NO_COPY(VM);
  };
}

