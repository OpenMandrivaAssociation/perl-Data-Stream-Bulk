%define upstream_name    Data-Stream-Bulk
%define upstream_version 0.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    L<Path::Class::Dir> traversal
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Moose)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Test::use::ok)
BuildRequires: perl(namespace::clean)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module tries to find middle ground between one at a time and all at
once processing of data sets.

The purpose of this module is to avoid the overhead of implementing an
iterative api when this isn't necessary, without breaking forward
compatibility in case that becomes necessary later on.

The API optimizes for when a data set typically fits in memory and is
returned as an array, but the consumer cannot assume that the data set is
bounded.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*


