# Created by pyp2rpm-1.1.0b

%global underscore_version %{lua:version = rpm.expand("%{flocker_version}"):gsub("-","_"); print(version)}

Name:           flocker
Version:        %{underscore_version}
Release:        1%{?dist}
Summary:        Docker orchestration and volume management
BuildArch:      noarch

License:        Proprietary
URL:            https://hybridcluster.github.io/
Source0:        Flocker-%{flocker_version}.tar.gz

BuildRequires:  python-devel

BuildRequires:  python
BuildRequires:  python-setuptools
# For tests
BuildRequires:  python-twisted
BuildRequires:  python-eliot >= 0.4.0, python-eliot < 0.5.0
BuildRequires:  python-characteristic
BuildRequires:  pytz
BuildRequires:  python-ipaddr
BuildRequires:  python-netifaces
# See https://github.com/hybridlogic/flocker/issues/85
BuildRequires:  docker-io

Requires:       python
Requires:       python-twisted
Requires:       python-eliot >= 0.4.0, python-eliot < 0.5.0
Requires:       python-characteristic
Requires:       pytz
Requires:       python-ipaddr
Requires:       python-netifaces
Requires:       docker-io
Requires:       /sbin/iptables
Requires:       geard

%description
probably a replication-based fail-over product


%prep
%setup -q -n Flocker-%{flocker_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info



%build
CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%check
trial flocker


%files
%doc README.rst

%{_bindir}/flocker-volume
%{python2_sitelib}/flocker
%{python2_sitelib}/Flocker-%{underscore_version}-py?.?.egg-info

%changelog
* Tue Jun 10 2014 Tom Prince - %{underscore_version}-1%{?dist}
- Development version