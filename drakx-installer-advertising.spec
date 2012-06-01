%define name drakx-installer-advertising
%define version 2012.0
%define release %mkrel 1

Summary: DrakX installer advertising files
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.xz
License: GPL
Group: Development/Other
Url: http://wiki.mandriva.com/Tools/DrakX
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
advertising files needed to build Mandriva installer (DrakX)

%prep
%setup -q

%install
rm -rf %{buildroot}

dest=%{buildroot}%{_datadir}/%name
mkdir -p $dest
make install ROOTDEST=$dest

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/%name


