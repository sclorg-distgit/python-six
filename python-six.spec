%{?scl:%scl_package python-six}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}python-six
Version:        1.3.0
Release:        3%{?dist}
Summary:        Python 2 and 3 compatibility utilities

Group:          Development/Languages
License:        MIT
URL:            http://pypi.python.org/pypi/six/
Source0:        http://pypi.python.org/packages/source/s/six/six-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
# RHSCL: pytest and tkinter are not in scl -- disable tests
# For use by selftests:
#BuildRequires:  pytest
#BuildRequires:  tkinter
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}

%description
python-six provides simple utilities for wrapping over differences between
Python 2 and Python 3.

This is the Python 2 build of the module.

%prep
%setup -q -n six-%{version}

%build
%{?scl:scl enable %{scl} - << \EOF}
%{__python} setup.py build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - << \EOF}
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT \
    --install-purelib %{python_sitelib}
%{?scl:EOF}

# disable tests: devassist09 doesn't contain pytest and tkinter
#%%check
#py.test -rfsxX test_six.py
#%if 0%{?with_python3}
#pushd %{py3dir}
#py.test-%{python3_version} -rfsxX test_six.py
#popd
#%endif

%files
%doc LICENSE README documentation/index.rst
%{python_sitelib}/*


%changelog
* Wed May 21 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.0-3
- Rebuilt for devassist09

* Wed Nov 13 2013 Tomas Tomecek <ttomecek@redhat.com> - 1.3.0-2
- RHSCL-1.1 build

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


