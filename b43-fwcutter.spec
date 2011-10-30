Name:           b43-fwcutter
Version:        015
Release:        0.1%{?dist}.R
Summary:        Firmware extraction tool for Broadcom wireless driver

Group:          System Environment/Base
License:        BSD
URL:            http://bu3sch.de/b43/fwcutter/
Source0:        http://bu3sch.de/b43/fwcutter/%{name}-%{version}.tar.bz2
Source1:        README.Fedora
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This package contains the 'b43-fwcutter' tool which is used to
extract firmware for the Broadcom network devices.

See the README.Fedora file shipped in the package's documentation for
instructions on using this tool.

%prep
%setup -q

cp %{SOURCE1} .

%build
CFLAGS="$RPM_OPT_FLAGS" make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m0755 b43-fwcutter $RPM_BUILD_ROOT%{_bindir}/b43-fwcutter
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m0644 b43-fwcutter.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/b43-fwcutter
%{_mandir}/man1/*
%doc COPYING README README.Fedora

%changelog
* Sun Oct 30 2011 Alexei Panov <me AT elemc DOT name> - 015-1
- Updata for b43-fwcutter-015

* Wed Mar 23 2011 John W. Linville <linville@redhat.com> 014-1
- Update for b43-fwcutter-014
- Remove patch to add COPYING file (now in upstream repository)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 013-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 26 2010 John W. Linville <linville@redhat.com> 013-2
- Add COPYING file

* Mon Apr 19 2010 John W. Linville <linville@redhat.com> 013-1
- Update for b43-fwcutter-013

* Fri Aug 28 2009 Bill Nottingham <notting@redhat.com> 012-2
- Update with some patches from git

* Mon Aug 24 2009 John W. Linville <linville@redhat.com> 012-1
- Update for b43-fwcutter-012

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 011-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May  7 2009 Ville Skyttä <ville.skytta at iki.fi> - 011-5
- Build with $RPM_OPT_FLAGS.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 011-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 15 2008 John W. Linville <linville@redhat.com> 011-3
- Update for b43-fwcutter-011

* Mon Jan 21 2008 John W. Linville <linville@redhat.com> 010-2
- Update for b43-fwcutter-010

* Thu Aug 23 2007 John W. Linville <linville@redhat.com> 008-1
- Import skeleton from bcm43xx-fwcutter-006-3
- Initial build
