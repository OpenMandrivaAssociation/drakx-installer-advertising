%define	family	drakx-installer
Summary:	DrakX installer advertising files
Name:		%{family}-advertising
Version:	2012.0
Release:	3
Source0:	%{name}-%{version}.tar.xz
License:	GPLv2+
Group:		Development/Other
Url:		http://wiki.mandriva.com/Tools/DrakX
BuildArch:	noarch

%description
Advertising files needed to build the Mandriva installer (DrakX).

%prep
%setup -q

%build

%install
%makeinstall_std -C advertising

# quite lame, but whatever..
# we'll just create some hard links here in order to make it simple to just
# copy the files with the same layout into install media
if [ -d %{buildroot}%{_prefix}/lib64/%{family}/root/install/extra/advertising/ ]; then
	lib1=lib64
	lib2=lib
else
	lib1=lib
	lib2=lib64
fi

mkdir -p %{buildroot}%{_prefix}/${lib2}/%{family}/root/install/extra/advertising/
for f in %{buildroot}%{_prefix}/${lib1}/%{family}/root/install/extra/advertising/*; do
	ln $f `echo $f|sed -e "s/$lib1/$lib2/"`
done

%files
%dir %{_prefix}/lib/%{family}
%dir %{_prefix}/lib64/%{family}
%dir %{_prefix}/lib/%{family}/root
%dir %{_prefix}/lib64/%{family}/root
%dir %{_prefix}/lib/%{family}/root/install
%dir %{_prefix}/lib64/%{family}/root/install
%dir %{_prefix}/lib/%{family}/root/install/extra
%dir %{_prefix}/lib64/%{family}/root/install/extra
%dir %{_prefix}/lib/%{family}/root/install/extra/advertising
%dir %{_prefix}/lib64/%{family}/root/install/extra/advertising
%{_prefix}/lib/%{family}/root/install/extra/advertising/*
%{_prefix}/lib64/%{family}/root/install/extra/advertising/*
