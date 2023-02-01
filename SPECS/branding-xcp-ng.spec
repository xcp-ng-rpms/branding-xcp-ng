Name:           branding-xcp-ng
Version:        8.3.0
Release:        2
Summary:        XCP-ng branding
License:        ISC
URL:            https://github.com/xcp-ng-rpms/branding-xcp-ng

Source0:        branding
Source1:        EULA
Source2:        LICENSES
Source3:        branding-compile.py
Source4:        brand-directory.py

BuildArch:      noarch
Requires:       python

%description
This package contains branding information for XCP-ng.

%build

%install
%{__install} -D -m 0644 %{SOURCE0} %{buildroot}%{_usrsrc}/branding/branding
%{__install} -D -m 0755 %{SOURCE4} %{buildroot}%{_usrsrc}/branding/brand-directory.py
%{__install} -D -m 0755 %{SOURCE3} %{buildroot}%{_usrsrc}/branding/branding-compile.py
%{__install} -D -m 0644 %{SOURCE1} %{buildroot}%{_usrsrc}/branding/EULA
%{__install} -D -m 0644 %{SOURCE2} %{buildroot}%{_usrsrc}/branding/LICENSES

%files
%{_usrsrc}/branding/branding
%{_usrsrc}/branding/brand-directory.py
%{_usrsrc}/branding/branding-compile.py
%{_usrsrc}/branding/EULA
%{_usrsrc}/branding/LICENSES
%exclude %{_usrsrc}/branding/*.pyc
%exclude %{_usrsrc}/branding/*.pyo

%changelog
* Wed Feb 01 2023 Yann Dirson <yann.dirson@vates.fr> - 8.3.0-2
- Remove usage of "upstream" tarball to avoid versionning confusion

* Thu Sep 01 2022 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.3.0-1
- Update for XCP-ng 8.3.0

* Tue Feb 15 2022 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.2.1-2
- Update year to 2022

* Tue Jan 04 2021 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.2.1-1
- Update for XCP-ng 8.2.1

* Tue Jun 30 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.2.0-1
- Update for XCP-ng 8.2.0

* Fri Dec 20 2019 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.1.0-1
- Update for XCP-ng 8.1.0
- Add EULA and LICENSES files

* Thu Apr 25 2019 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.0.0-2
- Update for XCP-ng 8.0.0
- Clean spec file: remove Group and BuildRoot definitions
- Remove 'dist' macro since it's built before xcp-ng-release

* Tue Dec 25 2018 Robin Lee <cheeselee@fedoraproject.org> - 7.6.0-2
- Change to noarch

* Wed Sep 12 2018 Samuel Verschelde <stormi-xcp@ylix.fr> - 7.6.0-1
- Update for XCP-ng 7.6.0

* Thu Jun 21 2018 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.0.1-1
- Update for XCP-ng 7.5.0

* Sun Apr 29 2018 John Else <john.else@gmail.com> - 1.0.0-1
- Initial package
