%define baserelease 1
#build with --define 'testbuild 1' to have a timestamp appended to release
%if 0%{?testbuild}
%define release %{baserelease}.%(date +%%Y%%m%%d.%%H%%M.%%S)
%else
%define release %{baserelease}
%endif
Name: koji-theme-circle
Version: 2.1
Release: %{release}%{?dist}.1
License: GPLv2
Summary: Circle Linux koji theme
Group: Applications/Internet
Source: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Requires: koji-web

%description
Makes the circlelinux koji web ui unique

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Authors COPYING README
%{_datadir}/koji-themes/fedora-koji
%config(noreplace) /etc/httpd/conf.d/00kojifedora.conf


%changelog
* Thu Jan 22 2014 James Xie<james@cclinux.org> - 2.1-1
- add circle logo and theme color
- fix spec for circle

* Thu Jan 22 2014 Dennis Gilmore <dennis@ausil.us> - 2.1-1
- update httpd config for apache 2.4

* Fri Feb 03 2012 Dennis Gilmore <dennis@ausil.us> 2.0-1
- pull in theme from ryan

* Mon Aug 24 2009 Dennis Gilmore <dennis@ausil.us> - 1.3-2
- add powered by koji button. 
- use new logo

* Fri Jul 31 2009 Dennis Gilmore <dennis@ausil.us> - 1.3-1
-initial build
