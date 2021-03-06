


                              _/Oo>
                             /(MM)
                            A___/       m a g p i e
                    _______AV_h_h___________________________
                          AV
                         AV
                        AV


Magpie is a small dynamically-typed programming language built around
patterns, classes, and multimethods. From functional languages, it borrows
first-class functions, closures, expressions-for-everything, and quotations.
Its most novel feature is probably an extensible syntax. It runs on the JVM.

It looks a bit like this:

    // Generates the sequence of turns needed to draw a dragon curve.
    // See: http://en.wikipedia.org/wiki/Dragon_curve
    def dragon(0, _)
        ""
    end

    def dragon(n is Int, turn)
        dragon(n - 1, "R") + turn + dragon(n - 1, "L")
    end

    print(dragon(5, ""))

Its goal is to let you write code that's beautiful and easy to read, and to
allow you to seamlessly extend the language and libraries as you see fit.

You can learn more about the language at http://magpie-lang.org/.

## Getting Started

It should be pretty easy to get it up and running. You'll need to:

*   Pull down the code. It lives here: https://github.com/munificent/magpie

*   Build it. The repo includes an Eclipse project if that's your thing. If
    you rock the command-line, you can just do:

        $ cd magpie
        $ ant jar

*   Run it. Magpie is a command line app. After building the jar, you can run
    it by doing:

        $ ./magpie

If you run it with no arguments, it drops you into a simple REPL. Enter a
Magpie expression and it will immediately evaluate it. Since everything is an
expression, even things like class definitions, you can build entire programs
incrementally this way. Here's one to get you started:

    for i in 1 to(20) do print("<your name> is awesome!")

If you pass an argument to the app, it will assume it's a path to a script
file and it will load and execute it:

    $ ./magpie script/Hello.mag
