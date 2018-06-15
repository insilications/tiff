#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tiff
Version  : 4.0.9
Release  : 25
URL      : ftp://download.osgeo.org/libtiff/tiff-4.0.9.tar.gz
Source0  : ftp://download.osgeo.org/libtiff/tiff-4.0.9.tar.gz
Summary  : Tag Image File Format (TIFF) library.
Group    : Development/Tools
License  : libtiff
Requires: tiff-bin
Requires: tiff-lib
Requires: tiff-doc
BuildRequires : cmake
BuildRequires : libjpeg-turbo-dev
BuildRequires : mesa-dev
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(zlib)

BuildRequires : scons
BuildRequires : xz-dev
BuildRequires : zlib-dev
Patch1: cve-2017-17095.patch
Patch2: cve-2017-18013.patch
Patch3: cve-2018-5784.patch
Patch4: cve-2018-7456.patch

%description
TIFF Software Distribution
--------------------------
This file is just a placeholder; all the documentation is now in
HTML in the html directory.  To view the documentation point your
favorite WWW viewer at html/index.html;

%package bin
Summary: bin components for the tiff package.
Group: Binaries

%description bin
bin components for the tiff package.


%package dev
Summary: dev components for the tiff package.
Group: Development
Requires: tiff-lib
Requires: tiff-bin
Provides: tiff-devel

%description dev
dev components for the tiff package.


%package doc
Summary: doc components for the tiff package.
Group: Documentation

%description doc
doc components for the tiff package.


%package lib
Summary: lib components for the tiff package.
Group: Libraries

%description lib
lib components for the tiff package.


%prep
%setup -q -n tiff-4.0.9
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526024694
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1526024694
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fax2ps
/usr/bin/fax2tiff
/usr/bin/pal2rgb
/usr/bin/ppm2tiff
/usr/bin/raw2tiff
/usr/bin/tiff2bw
/usr/bin/tiff2pdf
/usr/bin/tiff2ps
/usr/bin/tiff2rgba
/usr/bin/tiffcmp
/usr/bin/tiffcp
/usr/bin/tiffcrop
/usr/bin/tiffdither
/usr/bin/tiffdump
/usr/bin/tiffinfo
/usr/bin/tiffmedian
/usr/bin/tiffset
/usr/bin/tiffsplit

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/*.hxx
/usr/lib64/libtiff.so
/usr/lib64/libtiffxx.so
/usr/lib64/pkgconfig/libtiff-4.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/tiff/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtiff.so.5
/usr/lib64/libtiff.so.5.3.0
/usr/lib64/libtiffxx.so.5
/usr/lib64/libtiffxx.so.5.3.0
