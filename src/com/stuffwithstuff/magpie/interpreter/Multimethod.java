package com.stuffwithstuff.magpie.interpreter;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import com.stuffwithstuff.magpie.util.Expect;

public class Multimethod {
  public List<Callable> getMethods() { return mMethods; }
  
  public void addMethod(Callable method) {
    mMethods.add(method);
  }
  
  public Obj invoke(Interpreter interpreter, Obj receiver, Obj arg) {
    Expect.notNull(receiver);
    
    // If we're given a right-hand argument, combine it with the receiver.
    // If not, this is a getter-style multimethod.
    if (arg != null) {
      arg = interpreter.createTuple(receiver, arg);
    } else {
      arg = receiver;
    }
    
    Callable method = select(interpreter, arg);
        
    if (method == null) {
      interpreter.error("NoMethodError", 
          "Could not find a method to match argument " + arg + ".");
    }

    return method.invoke(interpreter, arg);
  }
  
  private Callable select(Interpreter interpreter, Obj arg) {
    Expect.notNull(arg);
    
    List<Callable> applicable = new ArrayList<Callable>();
    for (Callable method : mMethods) {
      // If the callable has a lexical context, evaluate its pattern in that
      // context. That way pattern names can refer to local variables.
      EvalContext context = new EvalContext(method.getClosure());
      if (PatternTester.test(interpreter, method.getPattern(), arg, context)) {
        applicable.add(method);
      }
    }
    
    if (applicable.size() == 0) return null;

    linearize(interpreter, applicable);
    
    return applicable.get(0);
  }

  private void linearize(Interpreter interpreter, List<Callable> methods) {
    if (methods.size() <= 1) return;
    Collections.sort(methods, new MethodLinearizer(interpreter));
  }
  
  private final List<Callable> mMethods = new ArrayList<Callable>();
}