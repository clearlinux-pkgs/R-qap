#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-qap
Version  : 0.1.1
Release  : 21
URL      : https://cran.r-project.org/src/contrib/qap_0.1-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/qap_0.1-1.tar.gz
Summary  : Heuristics for the Quadratic Assignment Problem (QAP)
Group    : Development/Tools
License  : GPL-3.0
Requires: R-qap-lib = %{version}-%{release}
BuildRequires : R-assertthat
BuildRequires : R-rlang
BuildRequires : buildreq-R

%description
# qap - Heuristics for the Quadratic Assignment Problem (QAP) - R package
[![CRAN version](http://www.r-pkg.org/badges/version/qap)](https://cran.r-project.org/package=qap)
[![CRAN RStudio mirror downloads](http://cranlogs.r-pkg.org/badges/qap)](https://cran.r-project.org/package=qap)
[![Travis-CI Build Status](https://travis-ci.org/mhahsler/qap.svg?branch=master)](https://travis-ci.org/mhahsler/qap)
[![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/github/mhahsler/qap?branch=master&svg=true)](https://ci.appveyor.com/project/mhahsler/qap)

%package lib
Summary: lib components for the R-qap package.
Group: Libraries

%description lib
lib components for the R-qap package.


%prep
%setup -q -c -n qap

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556466666

%install
export SOURCE_DATE_EPOCH=1556466666
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library qap
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library qap
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library qap
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc qap || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/qap/DESCRIPTION
/usr/lib64/R/library/qap/INDEX
/usr/lib64/R/library/qap/Meta/Rd.rds
/usr/lib64/R/library/qap/Meta/features.rds
/usr/lib64/R/library/qap/Meta/hsearch.rds
/usr/lib64/R/library/qap/Meta/links.rds
/usr/lib64/R/library/qap/Meta/nsInfo.rds
/usr/lib64/R/library/qap/Meta/package.rds
/usr/lib64/R/library/qap/NAMESPACE
/usr/lib64/R/library/qap/NEWS.md
/usr/lib64/R/library/qap/R/qap
/usr/lib64/R/library/qap/R/qap.rdb
/usr/lib64/R/library/qap/R/qap.rdx
/usr/lib64/R/library/qap/help/AnIndex
/usr/lib64/R/library/qap/help/aliases.rds
/usr/lib64/R/library/qap/help/paths.rds
/usr/lib64/R/library/qap/help/qap.rdb
/usr/lib64/R/library/qap/help/qap.rdx
/usr/lib64/R/library/qap/html/00Index.html
/usr/lib64/R/library/qap/html/R.css
/usr/lib64/R/library/qap/qaplib/bur26a.dat
/usr/lib64/R/library/qap/qaplib/bur26a.sln
/usr/lib64/R/library/qap/qaplib/bur26b.dat
/usr/lib64/R/library/qap/qaplib/bur26b.sln
/usr/lib64/R/library/qap/qaplib/bur26c.dat
/usr/lib64/R/library/qap/qaplib/bur26c.sln
/usr/lib64/R/library/qap/qaplib/bur26d.dat
/usr/lib64/R/library/qap/qaplib/bur26d.sln
/usr/lib64/R/library/qap/qaplib/bur26e.dat
/usr/lib64/R/library/qap/qaplib/bur26e.sln
/usr/lib64/R/library/qap/qaplib/bur26f.dat
/usr/lib64/R/library/qap/qaplib/bur26f.sln
/usr/lib64/R/library/qap/qaplib/bur26g.dat
/usr/lib64/R/library/qap/qaplib/bur26g.sln
/usr/lib64/R/library/qap/qaplib/bur26h.dat
/usr/lib64/R/library/qap/qaplib/bur26h.sln
/usr/lib64/R/library/qap/qaplib/chr12a.dat
/usr/lib64/R/library/qap/qaplib/chr12a.sln
/usr/lib64/R/library/qap/qaplib/chr12b.dat
/usr/lib64/R/library/qap/qaplib/chr12b.sln
/usr/lib64/R/library/qap/qaplib/chr12c.dat
/usr/lib64/R/library/qap/qaplib/chr12c.sln
/usr/lib64/R/library/qap/qaplib/chr15a.dat
/usr/lib64/R/library/qap/qaplib/chr15a.sln
/usr/lib64/R/library/qap/qaplib/chr15b.dat
/usr/lib64/R/library/qap/qaplib/chr15b.sln
/usr/lib64/R/library/qap/qaplib/chr15c.dat
/usr/lib64/R/library/qap/qaplib/chr15c.sln
/usr/lib64/R/library/qap/qaplib/chr18a.dat
/usr/lib64/R/library/qap/qaplib/chr18a.sln
/usr/lib64/R/library/qap/qaplib/chr18b.dat
/usr/lib64/R/library/qap/qaplib/chr18b.sln
/usr/lib64/R/library/qap/qaplib/chr20a.dat
/usr/lib64/R/library/qap/qaplib/chr20a.sln
/usr/lib64/R/library/qap/qaplib/chr20b.dat
/usr/lib64/R/library/qap/qaplib/chr20b.sln
/usr/lib64/R/library/qap/qaplib/chr20c.dat
/usr/lib64/R/library/qap/qaplib/chr20c.sln
/usr/lib64/R/library/qap/qaplib/chr22a.dat
/usr/lib64/R/library/qap/qaplib/chr22a.sln
/usr/lib64/R/library/qap/qaplib/chr22b.dat
/usr/lib64/R/library/qap/qaplib/chr22b.sln
/usr/lib64/R/library/qap/qaplib/chr25a.dat
/usr/lib64/R/library/qap/qaplib/chr25a.sln
/usr/lib64/R/library/qap/qaplib/els19.dat
/usr/lib64/R/library/qap/qaplib/els19.sln
/usr/lib64/R/library/qap/qaplib/esc128.dat
/usr/lib64/R/library/qap/qaplib/esc128.sln
/usr/lib64/R/library/qap/qaplib/esc16a.dat
/usr/lib64/R/library/qap/qaplib/esc16a.sln
/usr/lib64/R/library/qap/qaplib/esc16b.dat
/usr/lib64/R/library/qap/qaplib/esc16b.sln
/usr/lib64/R/library/qap/qaplib/esc16c.dat
/usr/lib64/R/library/qap/qaplib/esc16c.sln
/usr/lib64/R/library/qap/qaplib/esc16d.dat
/usr/lib64/R/library/qap/qaplib/esc16d.sln
/usr/lib64/R/library/qap/qaplib/esc16e.dat
/usr/lib64/R/library/qap/qaplib/esc16e.sln
/usr/lib64/R/library/qap/qaplib/esc16f.dat
/usr/lib64/R/library/qap/qaplib/esc16f.sln
/usr/lib64/R/library/qap/qaplib/esc16g.dat
/usr/lib64/R/library/qap/qaplib/esc16g.sln
/usr/lib64/R/library/qap/qaplib/esc16h.dat
/usr/lib64/R/library/qap/qaplib/esc16h.sln
/usr/lib64/R/library/qap/qaplib/esc16i.dat
/usr/lib64/R/library/qap/qaplib/esc16i.sln
/usr/lib64/R/library/qap/qaplib/esc16j.dat
/usr/lib64/R/library/qap/qaplib/esc16j.sln
/usr/lib64/R/library/qap/qaplib/esc32a.dat
/usr/lib64/R/library/qap/qaplib/esc32b.dat
/usr/lib64/R/library/qap/qaplib/esc32c.dat
/usr/lib64/R/library/qap/qaplib/esc32d.dat
/usr/lib64/R/library/qap/qaplib/esc32e.dat
/usr/lib64/R/library/qap/qaplib/esc32e.sln
/usr/lib64/R/library/qap/qaplib/esc32g.dat
/usr/lib64/R/library/qap/qaplib/esc32g.sln
/usr/lib64/R/library/qap/qaplib/esc32h.dat
/usr/lib64/R/library/qap/qaplib/esc64a.dat
/usr/lib64/R/library/qap/qaplib/had12.dat
/usr/lib64/R/library/qap/qaplib/had12.sln
/usr/lib64/R/library/qap/qaplib/had14.dat
/usr/lib64/R/library/qap/qaplib/had14.sln
/usr/lib64/R/library/qap/qaplib/had16.dat
/usr/lib64/R/library/qap/qaplib/had16.sln
/usr/lib64/R/library/qap/qaplib/had18.dat
/usr/lib64/R/library/qap/qaplib/had18.sln
/usr/lib64/R/library/qap/qaplib/had20.dat
/usr/lib64/R/library/qap/qaplib/had20.sln
/usr/lib64/R/library/qap/qaplib/kra30a.dat
/usr/lib64/R/library/qap/qaplib/kra30a.sln
/usr/lib64/R/library/qap/qaplib/kra30b.dat
/usr/lib64/R/library/qap/qaplib/kra30b.sln
/usr/lib64/R/library/qap/qaplib/kra32.dat
/usr/lib64/R/library/qap/qaplib/kra32.sln
/usr/lib64/R/library/qap/qaplib/lipa20a.dat
/usr/lib64/R/library/qap/qaplib/lipa20a.sln
/usr/lib64/R/library/qap/qaplib/lipa20b.dat
/usr/lib64/R/library/qap/qaplib/lipa20b.sln
/usr/lib64/R/library/qap/qaplib/lipa30a.dat
/usr/lib64/R/library/qap/qaplib/lipa30a.sln
/usr/lib64/R/library/qap/qaplib/lipa30b.dat
/usr/lib64/R/library/qap/qaplib/lipa30b.sln
/usr/lib64/R/library/qap/qaplib/lipa40a.dat
/usr/lib64/R/library/qap/qaplib/lipa40a.sln
/usr/lib64/R/library/qap/qaplib/lipa40b.dat
/usr/lib64/R/library/qap/qaplib/lipa40b.sln
/usr/lib64/R/library/qap/qaplib/lipa50a.dat
/usr/lib64/R/library/qap/qaplib/lipa50a.sln
/usr/lib64/R/library/qap/qaplib/lipa50b.dat
/usr/lib64/R/library/qap/qaplib/lipa50b.sln
/usr/lib64/R/library/qap/qaplib/lipa60a.dat
/usr/lib64/R/library/qap/qaplib/lipa60a.sln
/usr/lib64/R/library/qap/qaplib/lipa60b.dat
/usr/lib64/R/library/qap/qaplib/lipa60b.sln
/usr/lib64/R/library/qap/qaplib/lipa70a.dat
/usr/lib64/R/library/qap/qaplib/lipa70a.sln
/usr/lib64/R/library/qap/qaplib/lipa70b.dat
/usr/lib64/R/library/qap/qaplib/lipa70b.sln
/usr/lib64/R/library/qap/qaplib/lipa80a.dat
/usr/lib64/R/library/qap/qaplib/lipa80a.sln
/usr/lib64/R/library/qap/qaplib/lipa80b.dat
/usr/lib64/R/library/qap/qaplib/lipa80b.sln
/usr/lib64/R/library/qap/qaplib/lipa90a.dat
/usr/lib64/R/library/qap/qaplib/lipa90a.sln
/usr/lib64/R/library/qap/qaplib/lipa90b.dat
/usr/lib64/R/library/qap/qaplib/lipa90b.sln
/usr/lib64/R/library/qap/qaplib/nug12.dat
/usr/lib64/R/library/qap/qaplib/nug12.sln
/usr/lib64/R/library/qap/qaplib/nug14.dat
/usr/lib64/R/library/qap/qaplib/nug14.sln
/usr/lib64/R/library/qap/qaplib/nug15.dat
/usr/lib64/R/library/qap/qaplib/nug15.sln
/usr/lib64/R/library/qap/qaplib/nug16a.dat
/usr/lib64/R/library/qap/qaplib/nug16a.sln
/usr/lib64/R/library/qap/qaplib/nug16b.dat
/usr/lib64/R/library/qap/qaplib/nug16b.sln
/usr/lib64/R/library/qap/qaplib/nug17.dat
/usr/lib64/R/library/qap/qaplib/nug17.sln
/usr/lib64/R/library/qap/qaplib/nug18.dat
/usr/lib64/R/library/qap/qaplib/nug18.sln
/usr/lib64/R/library/qap/qaplib/nug20.dat
/usr/lib64/R/library/qap/qaplib/nug20.sln
/usr/lib64/R/library/qap/qaplib/nug21.dat
/usr/lib64/R/library/qap/qaplib/nug21.sln
/usr/lib64/R/library/qap/qaplib/nug22.dat
/usr/lib64/R/library/qap/qaplib/nug22.sln
/usr/lib64/R/library/qap/qaplib/nug24.dat
/usr/lib64/R/library/qap/qaplib/nug24.sln
/usr/lib64/R/library/qap/qaplib/nug25.dat
/usr/lib64/R/library/qap/qaplib/nug25.sln
/usr/lib64/R/library/qap/qaplib/nug27.dat
/usr/lib64/R/library/qap/qaplib/nug27.sln
/usr/lib64/R/library/qap/qaplib/nug28.dat
/usr/lib64/R/library/qap/qaplib/nug28.sln
/usr/lib64/R/library/qap/qaplib/nug30.dat
/usr/lib64/R/library/qap/qaplib/nug30.sln
/usr/lib64/R/library/qap/qaplib/rou12.dat
/usr/lib64/R/library/qap/qaplib/rou12.sln
/usr/lib64/R/library/qap/qaplib/rou15.dat
/usr/lib64/R/library/qap/qaplib/rou15.sln
/usr/lib64/R/library/qap/qaplib/rou20.dat
/usr/lib64/R/library/qap/qaplib/rou20.sln
/usr/lib64/R/library/qap/qaplib/scr12.dat
/usr/lib64/R/library/qap/qaplib/scr12.sln
/usr/lib64/R/library/qap/qaplib/scr15.dat
/usr/lib64/R/library/qap/qaplib/scr15.sln
/usr/lib64/R/library/qap/qaplib/scr20.dat
/usr/lib64/R/library/qap/qaplib/scr20.sln
/usr/lib64/R/library/qap/qaplib/sko100a.dat
/usr/lib64/R/library/qap/qaplib/sko100a.sln
/usr/lib64/R/library/qap/qaplib/sko100b.dat
/usr/lib64/R/library/qap/qaplib/sko100b.sln
/usr/lib64/R/library/qap/qaplib/sko100c.dat
/usr/lib64/R/library/qap/qaplib/sko100c.sln
/usr/lib64/R/library/qap/qaplib/sko100d.dat
/usr/lib64/R/library/qap/qaplib/sko100d.sln
/usr/lib64/R/library/qap/qaplib/sko100e.dat
/usr/lib64/R/library/qap/qaplib/sko100e.sln
/usr/lib64/R/library/qap/qaplib/sko100f.dat
/usr/lib64/R/library/qap/qaplib/sko100f.sln
/usr/lib64/R/library/qap/qaplib/sko42.dat
/usr/lib64/R/library/qap/qaplib/sko42.sln
/usr/lib64/R/library/qap/qaplib/sko49.dat
/usr/lib64/R/library/qap/qaplib/sko49.sln
/usr/lib64/R/library/qap/qaplib/sko56.dat
/usr/lib64/R/library/qap/qaplib/sko56.sln
/usr/lib64/R/library/qap/qaplib/sko64.dat
/usr/lib64/R/library/qap/qaplib/sko64.sln
/usr/lib64/R/library/qap/qaplib/sko72.dat
/usr/lib64/R/library/qap/qaplib/sko72.sln
/usr/lib64/R/library/qap/qaplib/sko81.dat
/usr/lib64/R/library/qap/qaplib/sko81.sln
/usr/lib64/R/library/qap/qaplib/sko90.dat
/usr/lib64/R/library/qap/qaplib/sko90.sln
/usr/lib64/R/library/qap/qaplib/ste36a.dat
/usr/lib64/R/library/qap/qaplib/ste36a.sln
/usr/lib64/R/library/qap/qaplib/ste36b.dat
/usr/lib64/R/library/qap/qaplib/ste36b.sln
/usr/lib64/R/library/qap/qaplib/ste36c.dat
/usr/lib64/R/library/qap/qaplib/ste36c.sln
/usr/lib64/R/library/qap/qaplib/tai100a.dat
/usr/lib64/R/library/qap/qaplib/tai100a.sln
/usr/lib64/R/library/qap/qaplib/tai100b.dat
/usr/lib64/R/library/qap/qaplib/tai100b.sln
/usr/lib64/R/library/qap/qaplib/tai10a.dat
/usr/lib64/R/library/qap/qaplib/tai10b.dat
/usr/lib64/R/library/qap/qaplib/tai12a.dat
/usr/lib64/R/library/qap/qaplib/tai12a.sln
/usr/lib64/R/library/qap/qaplib/tai12b.dat
/usr/lib64/R/library/qap/qaplib/tai12b.sln
/usr/lib64/R/library/qap/qaplib/tai150b.dat
/usr/lib64/R/library/qap/qaplib/tai150b.sln
/usr/lib64/R/library/qap/qaplib/tai15a.dat
/usr/lib64/R/library/qap/qaplib/tai15a.sln
/usr/lib64/R/library/qap/qaplib/tai15b.dat
/usr/lib64/R/library/qap/qaplib/tai15b.sln
/usr/lib64/R/library/qap/qaplib/tai17a.dat
/usr/lib64/R/library/qap/qaplib/tai17a.sln
/usr/lib64/R/library/qap/qaplib/tai20a.dat
/usr/lib64/R/library/qap/qaplib/tai20a.sln
/usr/lib64/R/library/qap/qaplib/tai20b.dat
/usr/lib64/R/library/qap/qaplib/tai20b.sln
/usr/lib64/R/library/qap/qaplib/tai256c.dat
/usr/lib64/R/library/qap/qaplib/tai256c.sln
/usr/lib64/R/library/qap/qaplib/tai25a.dat
/usr/lib64/R/library/qap/qaplib/tai25a.sln
/usr/lib64/R/library/qap/qaplib/tai25b.dat
/usr/lib64/R/library/qap/qaplib/tai25b.sln
/usr/lib64/R/library/qap/qaplib/tai30a.dat
/usr/lib64/R/library/qap/qaplib/tai30a.sln
/usr/lib64/R/library/qap/qaplib/tai30b.dat
/usr/lib64/R/library/qap/qaplib/tai30b.sln
/usr/lib64/R/library/qap/qaplib/tai35a.dat
/usr/lib64/R/library/qap/qaplib/tai35a.sln
/usr/lib64/R/library/qap/qaplib/tai35b.dat
/usr/lib64/R/library/qap/qaplib/tai35b.sln
/usr/lib64/R/library/qap/qaplib/tai40a.dat
/usr/lib64/R/library/qap/qaplib/tai40a.sln
/usr/lib64/R/library/qap/qaplib/tai40b.dat
/usr/lib64/R/library/qap/qaplib/tai40b.sln
/usr/lib64/R/library/qap/qaplib/tai50a.dat
/usr/lib64/R/library/qap/qaplib/tai50a.sln
/usr/lib64/R/library/qap/qaplib/tai50b.dat
/usr/lib64/R/library/qap/qaplib/tai50b.sln
/usr/lib64/R/library/qap/qaplib/tai60a.dat
/usr/lib64/R/library/qap/qaplib/tai60a.sln
/usr/lib64/R/library/qap/qaplib/tai60b.dat
/usr/lib64/R/library/qap/qaplib/tai60b.sln
/usr/lib64/R/library/qap/qaplib/tai64c.dat
/usr/lib64/R/library/qap/qaplib/tai64c.sln
/usr/lib64/R/library/qap/qaplib/tai80a.dat
/usr/lib64/R/library/qap/qaplib/tai80a.sln
/usr/lib64/R/library/qap/qaplib/tai80b.dat
/usr/lib64/R/library/qap/qaplib/tai80b.sln
/usr/lib64/R/library/qap/qaplib/tho150.dat
/usr/lib64/R/library/qap/qaplib/tho150.sln
/usr/lib64/R/library/qap/qaplib/tho30.dat
/usr/lib64/R/library/qap/qaplib/tho30.sln
/usr/lib64/R/library/qap/qaplib/tho40.dat
/usr/lib64/R/library/qap/qaplib/tho40.sln
/usr/lib64/R/library/qap/qaplib/wil100.dat
/usr/lib64/R/library/qap/qaplib/wil100.sln
/usr/lib64/R/library/qap/qaplib/wil50.dat
/usr/lib64/R/library/qap/qaplib/wil50.sln
/usr/lib64/R/library/qap/tests/testthat.R
/usr/lib64/R/library/qap/tests/testthat/test-qap.R
/usr/lib64/R/library/qap/tests/testthat/test-read_qaplib.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/qap/libs/qap.so
/usr/lib64/R/library/qap/libs/qap.so.avx2
