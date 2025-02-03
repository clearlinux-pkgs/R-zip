#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : R-zip
Version  : 2.3.2
Release  : 54
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/zip_2.3.2.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/zip_2.3.2.tar.gz
Summary  : Cross-Platform 'zip' Compression
Group    : Development/Tools
License  : MIT
Requires: R-zip-lib = %{version}-%{release}
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
the 'zip' function, that does not require any additional external
    tools on any platform.

%package lib
Summary: lib components for the R-zip package.
Group: Libraries

%description lib
lib components for the R-zip package.


%prep
%setup -q -n zip
pushd ..
cp -a zip buildavx2
popd
pushd ..
cp -a zip buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1738599318

%install
export SOURCE_DATE_EPOCH=1738599318
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/zip/bin/cmdunzip
/V3/usr/lib64/R/library/zip/bin/cmdzip
/V4/usr/lib64/R/library/zip/bin/cmdunzip
/V4/usr/lib64/R/library/zip/bin/cmdzip
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
/usr/lib64/R/library/zip/example.zip
/usr/lib64/R/library/zip/help/AnIndex
/usr/lib64/R/library/zip/help/aliases.rds
/usr/lib64/R/library/zip/help/paths.rds
/usr/lib64/R/library/zip/help/zip.rdb
/usr/lib64/R/library/zip/help/zip.rdx
/usr/lib64/R/library/zip/html/00Index.html
/usr/lib64/R/library/zip/html/R.css
/usr/lib64/R/library/zip/tests/testthat.R
/usr/lib64/R/library/zip/tests/testthat/_snaps/ascii/inflate.md
/usr/lib64/R/library/zip/tests/testthat/_snaps/inflate.md
/usr/lib64/R/library/zip/tests/testthat/_snaps/utf8/inflate.md
/usr/lib64/R/library/zip/tests/testthat/fixtures/abs.zip
/usr/lib64/R/library/zip/tests/testthat/fixtures/msdos.zip
/usr/lib64/R/library/zip/tests/testthat/helper.R
/usr/lib64/R/library/zip/tests/testthat/test-errors.R
/usr/lib64/R/library/zip/tests/testthat/test-get-zip-data-path.R
/usr/lib64/R/library/zip/tests/testthat/test-get-zip-data.R
/usr/lib64/R/library/zip/tests/testthat/test-inflate.R
/usr/lib64/R/library/zip/tests/testthat/test-large-files.R
/usr/lib64/R/library/zip/tests/testthat/test-paths.R
/usr/lib64/R/library/zip/tests/testthat/test-special-dot.R
/usr/lib64/R/library/zip/tests/testthat/test-unzip-process.R
/usr/lib64/R/library/zip/tests/testthat/test-unzip.R
/usr/lib64/R/library/zip/tests/testthat/test-weird-paths.R
/usr/lib64/R/library/zip/tests/testthat/test-zip-list.R
/usr/lib64/R/library/zip/tests/testthat/test-zip-process.R
/usr/lib64/R/library/zip/tests/testthat/test-zip.R
/usr/lib64/R/library/zip/tests/testthat/test-zipr.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/zip/libs/zip.so
/V4/usr/lib64/R/library/zip/libs/zip.so
/usr/lib64/R/library/zip/libs/zip.so
