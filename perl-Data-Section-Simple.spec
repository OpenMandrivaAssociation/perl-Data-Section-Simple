%define upstream_name    Data-Section-Simple
%define upstream_version 0.07

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:    Read data from __DATA__
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker) >= 6.300.0
BuildRequires: perl(Test::More) >= 0.880.0
BuildRequires: perl(Test::Requires)
BuildArch:  noarch

%description
Data::Section::Simple is a simple module to extract data from '__DATA__'
section of the file.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.json META.yml MYMETA.yml README
%{_mandir}/man3/*
%perl_vendorlib/*
