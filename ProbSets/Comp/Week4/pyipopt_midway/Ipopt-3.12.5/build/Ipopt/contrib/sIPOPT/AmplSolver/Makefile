# Copyright (C) 2009, 2010 Hans Pirnay. 
# All Rights Reserved.
# This code is published under the Eclipse Public License.
#
# Author: Hans Pirnay, 2009-12-15


#############################################################################
# Do not modify anything below unless you know what you're doing.
prefix      = /c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build
exec_prefix = ${prefix}
libdir      = ${exec_prefix}/lib
bindir      = ${exec_prefix}/bin
CYGPATH_W   = echo
SRCDIR      = ../../../../../Ipopt/contrib/sIPOPT/AmplSolver
ipoptsrcdir  = $(SRCDIR)/../../../src
senssrcdir = $(SRCDIR)/../src

CXX         = g++
CXXFLAGS    = -O3 -pipe -DNDEBUG -pedantic-errors -Wparentheses -Wreturn-type -Wcast-qual -Wall -Wpointer-arith -Wwrite-strings -Wconversion -Wno-unknown-pragmas -Wno-long-long   -DIPOPT_BUILD
LDFLAGS     = $(CXXFLAGS) 

# Include directories (we use the CYGPATH_W variables to allow compilation with Windows compilers)
#   we also need some Ipopt headers that are not installed, so we add $(ipoptsrcdir)/Algorithm and $(ipoptsrcdir)/LinAlg
#INCL = `PKG_CONFIG_PATH=/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib64/pkgconfig:/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib/pkgconfig:/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/share/pkgconfig:/mingw64/lib/pkgconfig:/mingw64/share/pkgconfig  --cflags ipoptamplinterface` -I`$(CYGPATH_W) $(ipoptsrcdir)/Algorithm` -I`$(CYGPATH_W) $(ipoptsrcdir)/LinAlg` -I`$(CYGPATH_W) $(senssrcdir)` $(ADDINCFLAGS)
INCL = -I`$(CYGPATH_W) /c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/include/coin`  -I/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/include/coin/ThirdParty  -I/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/include/coin/ThirdParty          -I/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/include/coin/ThirdParty  -I`$(CYGPATH_W) $(ipoptsrcdir)/Algorithm` -I`$(CYGPATH_W) $(ipoptsrcdir)/LinAlg` -I`$(CYGPATH_W) $(senssrcdir)` $(ADDINCFLAGS)

# Linker flags
#LIBS = -lsipopt `PKG_CONFIG_PATH=/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib64/pkgconfig:/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib/pkgconfig:/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/share/pkgconfig:/mingw64/lib/pkgconfig:/mingw64/share/pkgconfig  --libs ipoptamplinterface`
#LIBS = -link -libpath:`$(CYGPATH_W) /c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib` libsipopt.lib libipoptamplinterface.lib libipopt.lib  -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinhsl -L/opt/build/x86_64-710-posix-seh-rt_v502/mingw64/opt/lib -L/opt/build/prerequisites/x86_64-zlib-static/lib -L/opt/build/prerequisites/x86_64-w64-mingw32-static/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0 -LC:/Strawberry/c/bin/../lib/gcc -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib/../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../.. -lgfortran -lmingw32 -lmoldname -lmingwex -lmsvcrt -lquadmath -lm -lpthread -ladvapi32 -lshell32 -luser32 -lkernel32 -liconv  -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinmetis  -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinblas -L/opt/build/x86_64-710-posix-seh-rt_v502/mingw64/opt/lib -L/opt/build/prerequisites/x86_64-zlib-static/lib -L/opt/build/prerequisites/x86_64-w64-mingw32-static/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0 -LC:/Strawberry/c/bin/../lib/gcc -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib/../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../.. -lgfortran -lmingw32 -lmoldname -lmingwex -lmsvcrt -lquadmath -lm -lpthread -ladvapi32 -lshell32 -luser32 -lkernel32 -liconv   -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinlapack -L/opt/build/x86_64-710-posix-seh-rt_v502/mingw64/opt/lib -L/opt/build/prerequisites/x86_64-zlib-static/lib -L/opt/build/prerequisites/x86_64-w64-mingw32-static/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0 -LC:/Strawberry/c/bin/../lib/gcc -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib/../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../.. -lgfortran -lmingw32 -lmoldname -lmingwex -lmsvcrt -lquadmath -lm -lpthread -ladvapi32 -lshell32 -luser32 -lkernel32 -liconv  -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinblas -L/opt/build/x86_64-710-posix-seh-rt_v502/mingw64/opt/lib -L/opt/build/prerequisites/x86_64-zlib-static/lib -L/opt/build/prerequisites/x86_64-w64-mingw32-static/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0 -LC:/Strawberry/c/bin/../lib/gcc -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib/../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../.. -lgfortran -lmingw32 -lmoldname -lmingwex -lmsvcrt -lquadmath -lm -lpthread -ladvapi32 -lshell32 -luser32 -lkernel32 -liconv   -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinblas -L/opt/build/x86_64-710-posix-seh-rt_v502/mingw64/opt/lib -L/opt/build/prerequisites/x86_64-zlib-static/lib -L/opt/build/prerequisites/x86_64-w64-mingw32-static/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0 -LC:/Strawberry/c/bin/../lib/gcc -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib/../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../.. -lgfortran -lmingw32 -lmoldname -lmingwex -lmsvcrt -lquadmath -lm -lpthread -ladvapi32 -lshell32 -luser32 -lkernel32 -liconv  -lm   -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinasl -lm  
LIBS = -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lsipopt -lipoptamplinterface -lipopt  -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinhsl -L/opt/build/x86_64-710-posix-seh-rt_v502/mingw64/opt/lib -L/opt/build/prerequisites/x86_64-zlib-static/lib -L/opt/build/prerequisites/x86_64-w64-mingw32-static/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0 -LC:/Strawberry/c/bin/../lib/gcc -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib/../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../.. -lgfortran -lmingw32 -lmoldname -lmingwex -lmsvcrt -lquadmath -lm -lpthread -ladvapi32 -lshell32 -luser32 -lkernel32 -liconv  -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinmetis  -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinblas -L/opt/build/x86_64-710-posix-seh-rt_v502/mingw64/opt/lib -L/opt/build/prerequisites/x86_64-zlib-static/lib -L/opt/build/prerequisites/x86_64-w64-mingw32-static/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0 -LC:/Strawberry/c/bin/../lib/gcc -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib/../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../.. -lgfortran -lmingw32 -lmoldname -lmingwex -lmsvcrt -lquadmath -lm -lpthread -ladvapi32 -lshell32 -luser32 -lkernel32 -liconv   -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinlapack -L/opt/build/x86_64-710-posix-seh-rt_v502/mingw64/opt/lib -L/opt/build/prerequisites/x86_64-zlib-static/lib -L/opt/build/prerequisites/x86_64-w64-mingw32-static/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0 -LC:/Strawberry/c/bin/../lib/gcc -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib/../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../.. -lgfortran -lmingw32 -lmoldname -lmingwex -lmsvcrt -lquadmath -lm -lpthread -ladvapi32 -lshell32 -luser32 -lkernel32 -liconv  -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinblas -L/opt/build/x86_64-710-posix-seh-rt_v502/mingw64/opt/lib -L/opt/build/prerequisites/x86_64-zlib-static/lib -L/opt/build/prerequisites/x86_64-w64-mingw32-static/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0 -LC:/Strawberry/c/bin/../lib/gcc -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib/../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../.. -lgfortran -lmingw32 -lmoldname -lmingwex -lmsvcrt -lquadmath -lm -lpthread -ladvapi32 -lshell32 -luser32 -lkernel32 -liconv   -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinblas -L/opt/build/x86_64-710-posix-seh-rt_v502/mingw64/opt/lib -L/opt/build/prerequisites/x86_64-zlib-static/lib -L/opt/build/prerequisites/x86_64-w64-mingw32-static/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0 -LC:/Strawberry/c/bin/../lib/gcc -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib/../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../../../x86_64-w64-mingw32/lib -LC:/Strawberry/c/bin/../lib/gcc/x86_64-w64-mingw32/7.1.0/../../.. -lgfortran -lmingw32 -lmoldname -lmingwex -lmsvcrt -lquadmath -lm -lpthread -ladvapi32 -lshell32 -luser32 -lkernel32 -liconv  -lm   -L/c/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/ProbSets/Comp/Week4/pyipopt_midway/Ipopt-3.12.5/build/lib -lcoinasl -lm  

#LIBTOOL = $(SHELL) $(top_builddir)/../libtool
#CXXLD = $(CXX)
#CXXLINK = $(LIBTOOL) --tag=CXX --mode=link $(CXXLD) $(AM_CXXFLAGS) \
#	$(CXXFLAGS) $(AM_LDFLAGS) $(LDFLAGS) -o $@

sIPOPT_LIB = libsipopt.so

sIPOPT_LIBNAME =$(sIPOPT_LIB).0.0.0

TARGET = ipopt_sens

OBJS   = SensAmplTNLP.o 

VPATH = $(SRCDIR):$(ipoptsrcdir)/Apps/AmplSolver

all: $(OBJS)

install: $(TARGET)
	if test -d $(bindir); then : ; else mkdir $(bindir); fi
	cp $(TARGET) $(bindir)

uninstall:
	rm -f $(bindir)/$(TARGET)

$(TARGET): $(OBJS) ampl_sipopt.cpp
	$(CXX) $(LDFLAGS) $(SRCDIR)/ampl_sipopt.cpp -o $(TARGET) $(OBJS) $(INCL) $(LIBS)

%.o: %.cpp 
	$(CXX) $(CXXFLAGS) $(INCL) -o $@ -c $^

clean:
	rm -f $(OBJS) $(TARGET)

distclean: clean
