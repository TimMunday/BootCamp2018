# Copyright (C) 2003, 2010 International Business Machines and others.
# All Rights Reserved.
# This file is distributed under the Eclipse Public License.

# $Id: Makefile.in 1875 2010-12-28 23:32:54Z andreasw $

##########################################################################
#    You can modify this example makefile to fit for your own program.   #
#    Usually, you only need to change the five CHANGEME entries below.   #
##########################################################################

# CHANGEME: This should be the name of your executable
EXE = hs071_f.exe

# CHANGEME: Here is the name of all object files corresponding to the source
#           code that you wrote in order to define the problem statement
OBJS = hs071_f.o

# CHANGEME: Additional libraries
ADDLIBS =

# CHANGEME: Additional flags for compilation (e.g., include flags)
ADDINCFLAGS =

##########################################################################
#  Usually, you don't have to change anything below.  Note that if you   #
#  change certain compiler options, you might have to recompile Ipopt.   #
##########################################################################

# Fortran Compiler options
F77 = gfortran

# Fotran Compiler options
FFLAGS = -O3 -pipe  

# additional Fortran Compiler options for linking
F77LINKFLAGS = 

# Include directories (we use the CYGPATH_W variables to allow compilation with Windows compilers)
#INCL = `PKG_CONFIG_PATH=/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib64/pkgconfig:/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib/pkgconfig:/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/share/pkgconfig:/mingw64/lib/pkgconfig:/mingw64/share/pkgconfig  --cflags ipopt` $(ADDINCFLAGS)
INCL = -I`$(CYGPATH_W) /c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/include/coin`  -I/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/include/coin/ThirdParty  -I/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/include/coin/ThirdParty         $(ADDINCFLAGS)

# Linker flags
#LIBS = `PKG_CONFIG_PATH=/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib64/pkgconfig:/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib/pkgconfig:/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/share/pkgconfig:/mingw64/lib/pkgconfig:/mingw64/share/pkgconfig  --libs ipopt` -lstdc++ -lm
LIBS = -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lipopt  -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinhsl -L/opt/build/x86_64-710-posix-seh-rt_v502/mingw64/opt/lib -L/opt/build/prerequisites/x86_64-zlib-static/lib -L/opt/build/prerequisites/x86_64-w64-mingw32-static/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0 -LC:/Strawberry/c/bin/../lib/gcc -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib/../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../.. -lgfortran -lmingw32 -lmoldname -lmingwex -lmsvcrt -lquadmath -lm -lpthread -ladvapi32 -lshell32 -luser32 -lkernel32 -liconv  -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinmetis  -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinblas -L/opt/build/x86_64-710-posix-seh-rt_v502/mingw64/opt/lib -L/opt/build/prerequisites/x86_64-zlib-static/lib -L/opt/build/prerequisites/x86_64-w64-mingw32-static/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0 -LC:/Strawberry/c/bin/../lib/gcc -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib/../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../.. -lgfortran -lmingw32 -lmoldname -lmingwex -lmsvcrt -lquadmath -lm -lpthread -ladvapi32 -lshell32 -luser32 -lkernel32 -liconv   -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinlapack -L/opt/build/x86_64-710-posix-seh-rt_v502/mingw64/opt/lib -L/opt/build/prerequisites/x86_64-zlib-static/lib -L/opt/build/prerequisites/x86_64-w64-mingw32-static/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0 -LC:/Strawberry/c/bin/../lib/gcc -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib/../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../.. -lgfortran -lmingw32 -lmoldname -lmingwex -lmsvcrt -lquadmath -lm -lpthread -ladvapi32 -lshell32 -luser32 -lkernel32 -liconv  -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinblas -L/opt/build/x86_64-710-posix-seh-rt_v502/mingw64/opt/lib -L/opt/build/prerequisites/x86_64-zlib-static/lib -L/opt/build/prerequisites/x86_64-w64-mingw32-static/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0 -LC:/Strawberry/c/bin/../lib/gcc -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib/../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../.. -lgfortran -lmingw32 -lmoldname -lmingwex -lmsvcrt -lquadmath -lm -lpthread -ladvapi32 -lshell32 -luser32 -lkernel32 -liconv   -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinblas -L/opt/build/x86_64-710-posix-seh-rt_v502/mingw64/opt/lib -L/opt/build/prerequisites/x86_64-zlib-static/lib -L/opt/build/prerequisites/x86_64-w64-mingw32-static/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0 -LC:/Strawberry/c/bin/../lib/gcc -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib/../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../.. -lgfortran -lmingw32 -lmoldname -lmingwex -lmsvcrt -lquadmath -lm -lpthread -ladvapi32 -lshell32 -luser32 -lkernel32 -liconv  -lm  -lstdc++ -lm

# The following is necessary under cygwin, if native compilers are used
CYGPATH_W = echo

all: $(EXE)

.SUFFIXES: .f .o .obj

$(EXE): $(OBJS)
	bla=;\
	for file in $(OBJS); do bla="$$bla `$(CYGPATH_W) $$file`"; done; \
	$(F77) $(F77LINKFLAGS) $(FFLAGS) -o $@ $$bla $(ADDLIBS) $(LIBS)

clean:
	rm -f $(EXE) $(OBJS) IPOPT.OUT

.f.o:
	$(F77) $(FFLAGS) $(INCL) -c -o $@ $<


.f.obj:
	$(F77) $(FFLAGS) $(INCL) -c -o $@ `$(CYGPATH_W) '$<'`
