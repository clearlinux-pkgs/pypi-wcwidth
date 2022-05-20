#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-wcwidth
Version  : 0.2.5
Release  : 47
URL      : https://files.pythonhosted.org/packages/89/38/459b727c381504f361832b9e5ace19966de1a235d73cdbdea91c771a1155/wcwidth-0.2.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/89/38/459b727c381504f361832b9e5ace19966de1a235d73cdbdea91c771a1155/wcwidth-0.2.5.tar.gz
Summary  : Measures the displayed width of unicode strings in a terminal
Group    : Development/Tools
License  : MIT
Requires: pypi-wcwidth-license = %{version}-%{release}
Requires: pypi-wcwidth-python = %{version}-%{release}
Requires: pypi-wcwidth-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
============
        Introduction
        ============
        
        This library is mainly for CLI programs that carefully produce output for
        Terminals, or make pretend to be an emulator.

%package license
Summary: license components for the pypi-wcwidth package.
Group: Default

%description license
license components for the pypi-wcwidth package.


%package python
Summary: python components for the pypi-wcwidth package.
Group: Default
Requires: pypi-wcwidth-python3 = %{version}-%{release}

%description python
python components for the pypi-wcwidth package.


%package python3
Summary: python3 components for the pypi-wcwidth package.
Group: Default
Requires: python3-core
Provides: pypi(wcwidth)

%description python3
python3 components for the pypi-wcwidth package.


%prep
%setup -q -n wcwidth-0.2.5
cd %{_builddir}/wcwidth-0.2.5
pushd ..
cp -a wcwidth-0.2.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653006243
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-wcwidth
cp %{_builddir}/wcwidth-0.2.5/LICENSE %{buildroot}/usr/share/package-licenses/pypi-wcwidth/7bab96cb701213538a91d3a771b9856b24879ca8
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-wcwidth/7bab96cb701213538a91d3a771b9856b24879ca8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
