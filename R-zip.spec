#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-zip
Version  : 2.2.0
Release  : 34
URL      : https://cran.r-project.org/src/contrib/zip_2.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/zip_2.2.0.tar.gz
Summary  : Cross-Platform 'zip' Compression
Group    : Development/Tools
License  : MIT
Requires: R-zip-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
for the 'zip' function, that does not require any additional
    external tools on any platform.

%package lib
Summary: lib components for the R-zip package.
Group: Libraries

%description lib
lib components for the R-zip package.


%prep
%setup -q -c -n zip
cd %{_builddir}/zip

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1622566920

%install
export SOURCE_DATE_EPOCH=1622566920
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library zip
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library zip
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library zip
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc zip || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/zip/DESCRIPTION
/usr/lib64/R/library/zip/INDEX
/usr/lib64/R/library/zip/LICENSE
/usr/lib64/R/library/zip/Meta/Rd.rds
/usr/lib64/R/library/zip/Meta/features.rds
/usr/lib64/R/library/zip/Meta/hsearch.rds
/usr/lib64/R/library/zip/Meta/links.rds
/usr/lib64/R/library/zip/Meta/nsInfo.rds
/usr/lib64/R/library/zip/Meta/package.rds
/usr/lib64/R/library/zip/NAMESPACE
/usr/lib64/R/library/zip/NEWS.md
/usr/lib64/R/library/zip/R/zip
/usr/lib64/R/library/zip/R/zip.rdb
/usr/lib64/R/library/zip/R/zip.rdx
/usr/lib64/R/library/zip/bin/cmdunzip
/usr/lib64/R/library/zip/bin/cmdzip
/usr/lib64/R/library/zip/doc/assets/extra.css
/usr/lib64/R/library/zip/doc/assets/rd.js
/usr/lib64/R/library/zip/example.zip
/usr/lib64/R/library/zip/help/AnIndex
/usr/lib64/R/library/zip/help/aliases.rds
/usr/lib64/R/library/zip/help/paths.rds
/usr/lib64/R/library/zip/help/zip.rdb
/usr/lib64/R/library/zip/help/zip.rdx
/usr/lib64/R/library/zip/html/00Index.html
/usr/lib64/R/library/zip/html/R.css
/usr/lib64/R/library/zip/tests/testthat.R
/usr/lib64/R/library/zip/tests/testthat/helper.R
/usr/lib64/R/library/zip/tests/testthat/test-errors.R
/usr/lib64/R/library/zip/tests/testthat/test-get-zip-data-path.R
/usr/lib64/R/library/zip/tests/testthat/test-get-zip-data.R
/usr/lib64/R/library/zip/tests/testthat/test-large-files.R
/usr/lib64/R/library/zip/tests/testthat/test-paths.R
/usr/lib64/R/library/zip/tests/testthat/test-unzip-process.R
/usr/lib64/R/library/zip/tests/testthat/test-unzip.R
/usr/lib64/R/library/zip/tests/testthat/test-zip-list.R
/usr/lib64/R/library/zip/tests/testthat/test-zip-process.R
/usr/lib64/R/library/zip/tests/testthat/test-zip.R
/usr/lib64/R/library/zip/tests/testthat/test-zipr.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/zip/libs/zip.so
/usr/lib64/R/library/zip/libs/zip.so.avx2
/usr/lib64/R/library/zip/libs/zip.so.avx512
