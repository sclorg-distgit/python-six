%{?scl:%scl_package python-%{modname}}
%{!?scl:%global pkg_name %{name}}
%global python3_pkgversion %{nil}

%global modname six

# SCL: Permanently disabled duo to missing dependencies
%bcond_with tests

%global python_wheelname %{modname}-%{version}-py2.py3-none-any.whl

Name:           %{?scl_prefix}python-%{modname}
Version:        1.12.0
Release:        10%{?dist}
Summary:        Python 2 and 3 compatibility utilities

License:        MIT
URL:            https://pypi.python.org/pypi/six
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{modname}; echo ${n:0:1})/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pip
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-wheel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-rpm-macros

%if %{with tests}
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-pytest
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-tkinter
%endif


%global _description \
%{pkg_name} provides simple utilities for wrapping over differences between\
Python 2 and Python 3.

%description %{_description}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{modname}-%{version}
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_build_wheel
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_install_wheel %{python_wheelname}
%{?scl:EOF}


%if %{with tests}
%check
%{?scl:scl enable %{scl} - << \EOF}
set -ex
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} -rfsxX test_six.py
%{?scl:EOF}
%endif


%files
%license LICENSE
%doc README.rst documentation/index.rst
%{python3_sitelib}/%{modname}-*.dist-info/
%{python3_sitelib}/%{modname}.py
%{python3_sitelib}/__pycache__/%{modname}.*


%changelog
* Mon Feb 03 2020 Tomas Orsava <torsava@redhat.com> - 1.12.0-10
- Import from the python38 module and modified for rh-python38 RHSCL
- Resolves: rhbz#1671025

* Fri Dec 13 2019 Tomas Orsava <torsava@redhat.com> - 1.12.0-9
- Exclude unsupported i686 arch

* Tue Nov 19 2019 Lumír Balhar <lbalhar@redhat.com> - 1.12.0-8
- Adjusted for Python 3.8 module in RHEL 8

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.0-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 26 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.0-6
- Reduce Python 2 build dependencies

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.0-5
- Rebuilt for Python 3.8

* Wed Aug 14 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.0-4
- Bootstrap for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 Yatin Karel <ykarel@redhat.com> - 1.12.0-1
- Update to 1.12.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 Miro Hrončok <mhroncok@redhat.com> - 1.11.0-5
- Rebuilt for Python 3.7

* Wed Jun 13 2018 Miro Hrončok <mhroncok@redhat.com> - 1.11.0-4
- Bootstrap for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 15 2017 Lumír Balhar <lbalhar@redhat.com> - 1.11.0-2
- Removed and obsoleted the platform-python subpackage

* Tue Sep 19 2017 Charalampos Stratakis <cstratak@redhat.com> - 1.11.0-1
- Update to 1.11.0

* Thu Aug 10 2017 Tomas Orsava <torsava@redhat.com> - 1.10.0-11
- Added the platform-python subpackage

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Petr Viktorin <pviktori@redhat.com> - 1.10.0-9
- Fix unversioned Python BuildRequires

* Mon Feb 13 2017 Charalampos Stratakis <cstratak@redhat.com> - 1.10.0-8
- Rebuild as wheel

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Charalampos Stratakis <cstratak@redhat.com> - 1.10.0-6
- Enable tests

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 1.10.0-5
- Rebuild for Python 3.6
- Disable python3 tests

* Tue Aug 09 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.10.0-4
- Modernize spec more
- Depend on system-python(abi)
- Cleanups

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 3 2016 Orion Poplawski <orion@cora.nwra.com> - 1.10.0-2
- Modernize spec
- Fix python3 package file ownership

* Fri Nov 13 2015 Slavek Kabrda <bkabrda@redhat.com> - 1.10.0-1
- Update to 1.10.0

* Tue Oct 13 2015 Robert Kuska <rkuska@redhat.com> - 1.9.0-4
- Rebuilt for Python3.5 rebuild

* Mon Jul 13 2015 Slavek Kabrda <bkabrda@redhat.com> - 1.9.0-3
- Added python2-six provide to python-six

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 23 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 1.9.0-1
- Upstream 1.9.0
- Packaging cleanups

* Fri Nov 14 2014 Slavek Kabrda <bkabrda@redhat.com> - 1.8.0-1
- upgrade to 1.8.0 (rhbz#1105861)

* Sun Aug  3 2014 Tom Callaway <spot@fedoraproject.org> - 1.7.3-2
- fix license handling

* Thu Jul 31 2014 Pádraig Brady <pbrady@redhat.com> - 1.7.3-1
- Latest upstream

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 08 2014 Orion Poplawski <orion@cora.nwra.com> - 1.6.1-2
- Rebuild for Python 3.4

* Tue Apr 29 2014 Matthias Runge <mrugne@redhat.com> - 1.6.1-1
- upgrade to 1.6.1 (rhbz#1076578)

* Fri Mar 07 2014 Matthias Runge <mrunge@redhat.com> - 1.5.2-1
- upgrade to 1.5.2 (rhbz#1048819)

* Mon Sep 16 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.4.1-1
- 1.4.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 21 2013 David Malcolm <dmalcolm@redhat.com> - 1.3.0-1
- 1.3.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 29 2012 David Malcolm <dmalcolm@redhat.com> - 1.2.0-1
- 1.2.0 (rhbz#852658)
- add %%check section

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 1.1.0-4
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Ralph Bean <rbean@redhat.com> - 1.1.0-2
- Conditionalized python3-six, allowing an el6 build.

* Tue Feb  7 2012 David Malcolm <dmalcolm@redhat.com> - 1.1.0-1
- 1.1.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 24 2011 David Malcolm <dmalcolm@redhat.com> - 1.0.0-1
- initial packaging

