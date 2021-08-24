import sys

# https://stackoverflow.com/questions/32234156/how-to-unimport-a-python-module-which-is-already-imported
def deimport(module_object=None,module=None,verbose=False):
    if module==None:
        module=module_object.__name__
    if verbose:
        print("Deimporting module: "+module)
        s=[gl for gl in sys.modules if gl.startswith(module+".")]
        print("Found the following modules in cache:",s)
        g=[gl for gl in globals() if gl.startswith(module+".")]
        print("Found the following modules global:",g)
    try:

        if module in sys.modules:
            sub = [s for s in sys.modules if s.startswith(module+".")]  
            del sys.modules[module]
            for s in sub:
                del sys.modules[s]
                try:
                    del globals()[s]
                except:
                    pass
            try:
                del globals()[module]
            except:
                pass
        if verbose:
            print("Deimporting module: "+module)
            s=[gl for gl in sys.modules if gl.startswith(module+".")]
            print("Now trying searching for the same module again in cache: ",s)
            g=[gl for gl in globals() if gl.startswith(module+".")]
            print("and in global:",g)
    except:
        pass

