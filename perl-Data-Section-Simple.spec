%define upstream_name    Data-Section-Simple
%define upstream_version 0.07

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

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

%changelog
* Sun Oct 19 2014 umeabot <umeabot> 0.70.0-4.mga5
+ Revision: 788657
- Rebuild to potentially add missing dependencies

* Wed Oct 15 2014 umeabot <umeabot> 0.70.0-3.mga5
+ Revision: 740299
- Second Mageia 5 Mass Rebuild

* Tue Sep 16 2014 umeabot <umeabot> 0.70.0-2.mga5
+ Revision: 684235
- Mageia 5 Mass Rebuild

* Tue May 06 2014 jquelin <jquelin> 0.70.0-1.mga5
+ Revision: 620510
- update to 0.07

* Tue Apr 15 2014 jquelin <jquelin> 0.60.0-1.mga5
+ Revision: 614695
- update to 0.06

* Sat Oct 19 2013 umeabot <umeabot> 0.50.0-2.mga4
+ Revision: 526853
- Mageia 4 Mass Rebuild

* Fri Jun 07 2013 jquelin <jquelin> 0.50.0-1.mga4
+ Revision: 438981
- update to 0.05

* Sun Jan 13 2013 umeabot <umeabot> 0.30.0-2.mga3
+ Revision: 365435
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Sat Apr 07 2012 jquelin <jquelin> 0.30.0-1.mga2
+ Revision: 229540
- imported package perl-Data-Section-Simple


* Sat Apr 07 2012 cpan2dist 0.03-1mga
- initial mageia release, generated with cpan2dist
