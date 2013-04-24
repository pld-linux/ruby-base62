%define	pkgname	base62
Summary:	module that monkeypatches Integer and String to add Base62 encoder
Name:		ruby-%{pkgname}
Version:	0.1.4
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	0aec615988ddc6b5ba837c049ee4d95c
URL:		http://github.com/jtzemp/base62
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Base62 monkeypatches Integer to add an Integer#base62_encode instance
method to encode an integer in the character set of 0-9 + A-Z + a-z.
It also monkeypatches String to add String#base62_decode to take the
string and turn it back into a valid integer.

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rdoc History.txt
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
