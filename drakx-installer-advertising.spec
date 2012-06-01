Summary:	DrakX installer advertising files
Name:		drakx-installer-advertising
Version:	2012.0
Release:	1
Source0:	%{name}-%{version}.tar.xz
License:	GPLv2+
Group:		Development/Other
Url:		http://wiki.mandriva.com/Tools/DrakX

%description
Advertising files needed to build the Mandriva installer (DrakX).

%prep
%setup -q

%build

%install
dest=%{buildroot}%{_datadir}/%{name}
make install ROOTDEST=$dest

%files
%{_datadir}/%name
