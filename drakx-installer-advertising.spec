%define name drakx-installer-advertising
%define version 0.3
%define release %mkrel 1

Summary: DrakX installer advertising files
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Development/Other
Url: http://wiki.mandriva.com/Tools/DrakX
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
advertising files needed to build Mandriva installer (DrakX)

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

dest=$RPM_BUILD_ROOT%{_datadir}/%name
mkdir -p $dest
make install ROOTDEST=$dest

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_datadir}/%name


