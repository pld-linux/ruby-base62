#
# Conditional build:
%bcond_without	tests		# build without tests

%define	pkgname	base62
Summary:	module that monkeypatches Integer and String to add Base62 encoder
Name:		ruby-%{pkgname}
Version:	1.0.0
Release:	2
License:	MIT
Group:		Development/Languages
Source0:	https://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	9848bfe0975daad5e17d5042506c1e85
URL:		https://github.com/jtzemp/base62
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	ruby-test-unit
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Base62 monkeypatches Integer to add an Integer#base62_encode instance
method to encode an integer in the character set of 0-9 + A-Z + a-z.
It also monkeypatches String to add String#base62_decode to take the
string and turn it back into a valid integer.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%if %{with tests}
ruby -Ilib -Itest -e 'require "rubygems"; require "test/unit"; require "base62_test"'
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGELOG.md
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
