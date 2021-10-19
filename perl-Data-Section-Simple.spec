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
%autosetup -p1 -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor

%make_build

%check
%make test

%install
%make_install

%files
%doc Changes LICENSE META.json META.yml MYMETA.yml README
%doc %{_mandir}/man3/*
%perl_vendorlib/*
