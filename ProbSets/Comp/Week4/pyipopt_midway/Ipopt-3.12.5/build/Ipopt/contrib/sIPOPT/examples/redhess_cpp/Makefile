# Copyright (C) 2010 Hans Pirnay
# All Rights Reserved.
# This file is distributed under the Eclipse Public License.


##########################################################################
#    You can modify this example makefile to fit for your own program.   #
#    Usually, you only need to change the five CHANGEME entries below.   #
##########################################################################

# CHANGEME: This should be the name of your executable
EXE = redhess_cpp.exe

# CHANGEME: Here is the name of all object files corresponding to the source
#           code that you wrote in order to define the problem statement
OBJS =  redhess_cpp.o \
	MySensTNLP.o

# CHANGEME: Additional libraries
ADDLIBS =

# CHANGEME: Additional flags for compilation (e.g., include flags)
ADDINCFLAGS =

##########################################################################
#  Usually, you don't have to change anything below.  Note that if you   #
#  change certain compiler options, you might have to recompile Ipopt.   #
##########################################################################

# C++ Compiler command
CXX = g++

# C++ Compiler options
CXXFLAGS = -O3 -pipe -DNDEBUG -pedantic-errors -Wparentheses -Wreturn-type -Wcast-qual -Wall -Wpointer-arith -Wwrite-strings -Wconversion -Wno-unknown-pragmas -Wno-long-long   -DIPOPT_BUILD

# additional C++ Compiler options for linking
CXXLINKFLAGS = 

SRCDIR = ../../../../../../Ipopt/contrib/sIPOPT/examples/redhess_cpp
ipoptsrcdir  = $(SRCDIR)/../../../../src
senssrcdir = $(SRCDIR)/../../src

# Include directories (we use the CYGPATH_W variables to allow compilation with Windows compilers)
#   we also need some Ipopt headers that are not installed, so we add $(ipoptsrcdir)/Algorithm and $(ipoptsrcdir)/LinAlg
#INCL = `PKG_CONFIG_PATH=/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib64/pkgconfig:/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib/pkgconfig:/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/share/pkgconfig:/mingw64/lib/pkgconfig:/mingw64/share/pkgconfig  --cflags ipopt` -I`$(CYGPATH_W) $(ipoptsrcdir)/Algorithm` -I`$(CYGPATH_W) $(ipoptsrcdir)/LinAlg` -I`$(CYGPATH_W) $(senssrcdir)` $(ADDINCFLAGS)
INCL = -I`$(CYGPATH_W) /c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/include/coin`  -I/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/include/coin/ThirdParty  -I/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/include/coin/ThirdParty         -I`$(CYGPATH_W) $(ipoptsrcdir)/Algorithm` -I`$(CYGPATH_W) $(ipoptsrcdir)/LinAlg` -I`$(CYGPATH_W) $(senssrcdir)` $(ADDINCFLAGS)

# Linker flags
#LIBS = -lsipopt `PKG_CONFIG_PATH=/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib64/pkgconfig:/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib/pkgconfig:/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/share/pkgconfig:/mingw64/lib/pkgconfig:/mingw64/share/pkgconfig  --libs ipopt`
#LIBS = -link -libpath:`$(CYGPATH_W) /c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib` libsipopt.lib libipopt.lib  -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinhsl -L/opt/build/x86_64-710-posix-seh-rt_v502/mingw64/opt/lib -L/opt/build/prerequisites/x86_64-zlib-static/lib -L/opt/build/prerequisites/x86_64-w64-mingw32-static/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0 -LC:/Strawberry/c/bin/../lib/gcc -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib/../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../.. -lgfortran -lmingw32 -lmoldname -lmingwex -lmsvcrt -lquadmath -lm -lpthread -ladvapi32 -lshell32 -luser32 -lkernel32 -liconv  -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinmetis  -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinblas -L/opt/build/x86_64-710-posix-seh-rt_v502/mingw64/opt/lib -L/opt/build/prerequisites/x86_64-zlib-static/lib -L/opt/build/prerequisites/x86_64-w64-mingw32-static/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0 -LC:/Strawberry/c/bin/../lib/gcc -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib/../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../.. -lgfortran -lmingw32 -lmoldname -lmingwex -lmsvcrt -lquadmath -lm -lpthread -ladvapi32 -lshell32 -luser32 -lkernel32 -liconv   -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinlapack -L/opt/build/x86_64-710-posix-seh-rt_v502/mingw64/opt/lib -L/opt/build/prerequisites/x86_64-zlib-static/lib -L/opt/build/prerequisites/x86_64-w64-mingw32-static/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0 -LC:/Strawberry/c/bin/../lib/gcc -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib/../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../.. -lgfortran -lmingw32 -lmoldname -lmingwex -lmsvcrt -lquadmath -lm -lpthread -ladvapi32 -lshell32 -luser32 -lkernel32 -liconv  -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinblas -L/opt/build/x86_64-710-posix-seh-rt_v502/mingw64/opt/lib -L/opt/build/prerequisites/x86_64-zlib-static/lib -L/opt/build/prerequisites/x86_64-w64-mingw32-static/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0 -LC:/Strawberry/c/bin/../lib/gcc -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib/../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../.. -lgfortran -lmingw32 -lmoldname -lmingwex -lmsvcrt -lquadmath -lm -lpthread -ladvapi32 -lshell32 -luser32 -lkernel32 -liconv   -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinblas -L/opt/build/x86_64-710-posix-seh-rt_v502/mingw64/opt/lib -L/opt/build/prerequisites/x86_64-zlib-static/lib -L/opt/build/prerequisites/x86_64-w64-mingw32-static/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0 -LC:/Strawberry/c/bin/../lib/gcc -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib/../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../.. -lgfortran -lmingw32 -lmoldname -lmingwex -lmsvcrt -lquadmath -lm -lpthread -ladvapi32 -lshell32 -luser32 -lkernel32 -liconv  -lm 
LIBS = -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lsipopt -lipopt  -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinhsl -L/opt/build/x86_64-710-posix-seh-rt_v502/mingw64/opt/lib -L/opt/build/prerequisites/x86_64-zlib-static/lib -L/opt/build/prerequisites/x86_64-w64-mingw32-static/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0 -LC:/Strawberry/c/bin/../lib/gcc -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib/../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../.. -lgfortran -lmingw32 -lmoldname -lmingwex -lmsvcrt -lquadmath -lm -lpthread -ladvapi32 -lshell32 -luser32 -lkernel32 -liconv  -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinmetis  -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinblas -L/opt/build/x86_64-710-posix-seh-rt_v502/mingw64/opt/lib -L/opt/build/prerequisites/x86_64-zlib-static/lib -L/opt/build/prerequisites/x86_64-w64-mingw32-static/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0 -LC:/Strawberry/c/bin/../lib/gcc -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib/../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../.. -lgfortran -lmingw32 -lmoldname -lmingwex -lmsvcrt -lquadmath -lm -lpthread -ladvapi32 -lshell32 -luser32 -lkernel32 -liconv   -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinlapack -L/opt/build/x86_64-710-posix-seh-rt_v502/mingw64/opt/lib -L/opt/build/prerequisites/x86_64-zlib-static/lib -L/opt/build/prerequisites/x86_64-w64-mingw32-static/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0 -LC:/Strawberry/c/bin/../lib/gcc -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib/../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../.. -lgfortran -lmingw32 -lmoldname -lmingwex -lmsvcrt -lquadmath -lm -lpthread -ladvapi32 -lshell32 -luser32 -lkernel32 -liconv  -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinblas -L/opt/build/x86_64-710-posix-seh-rt_v502/mingw64/opt/lib -L/opt/build/prerequisites/x86_64-zlib-static/lib -L/opt/build/prerequisites/x86_64-w64-mingw32-static/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0 -LC:/Strawberry/c/bin/../lib/gcc -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib/../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../.. -lgfortran -lmingw32 -lmoldname -lmingwex -lmsvcrt -lquadmath -lm -lpthread -ladvapi32 -lshell32 -luser32 -lkernel32 -liconv   -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinblas -L/opt/build/x86_64-710-posix-seh-rt_v502/mingw64/opt/lib -L/opt/build/prerequisites/x86_64-zlib-static/lib -L/opt/build/prerequisites/x86_64-w64-mingw32-static/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0 -LC:/Strawberry/c/bin/../lib/gcc -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib/../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../.. -lgfortran -lmingw32 -lmoldname -lmingwex -lmsvcrt -lquadmath -lm -lpthread -ladvapi32 -lshell32 -luser32 -lkernel32 -liconv  -lm 

# The following is necessary under cygwin, if native compilers are used
CYGPATH_W = echo

all: $(EXE)

.SUFFIXES: .cpp .c .o .obj

$(EXE): $(OBJS)
	bla=;\
	for file in $(OBJS); do bla="$$bla `$(CYGPATH_W) $$file`"; done; \
	$(CXX) $(CXXLINKFLAGS) $(CXXFLAGS) -o $@ $$bla $(ADDLIBS) $(LIBS)

clean:
	rm -rf $(EXE) $(OBJS)

.cpp.o:
	$(CXX) $(CXXFLAGS) $(INCL) -c -o $@ $<


.cpp.obj:
	$(CXX) $(CXXFLAGS) $(INCL) -c -o $@ `$(CYGPATH_W) '$<'`
