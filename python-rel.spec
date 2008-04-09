
%define		module rel

Summary:	A pure Python pyevent emulation module
Name:		python-%{module}
Version:	0.1.12
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	http://registeredeventlistener.googlecode.com/files/%{module}-%{version}.tar.gz
# Source0-md5:	8b06018efc4a1ca9441a1be0f0e70d8b
URL:		http://brbx.com/orbited/index.html
BuildRequires:	libevent-devel
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
Suggests:	orbited
%pyrequires_eq	python-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The rel module is a drop-in replacement for pyevent that completely
emulates pyevent's interface, behavior and functionality on any system
with Python. It will use pyevent if it's available, and if it's not
rel will use the fastest method supported by the system.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-*.egg-info
