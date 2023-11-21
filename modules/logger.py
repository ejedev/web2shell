from data import types


def splash():
    print(
        """
               o                  o           o  o
               O     .oOOo.       O           O  O
               O          O       o           o  o
               o          o       O           O  O
'o     O .oOo. OoOo.     O' .oOo  OoOo. .oOo. o  o
 O  o  o OooO' O   o    O   `Ooo. o   o OooO' O  O
 o  O  O O     o   O  .O        O o   O O     o  o
 `Oo'oO' `OoO' `OoO' oOoOoO `OoO' O   o `OoO' Oo Oo
---------------------------------------------------
                v0.1.2   @ejedev
        """
    )


def log(message: str, type: types.Status = types.Status.NONE, verbose: bool = False, verbosity: bool = False):
    if verbose and not verbosity:
        pass
    elif type == types.Status.NONE:
        print(message)
    else:
        print(f"{type.value} {message}")
