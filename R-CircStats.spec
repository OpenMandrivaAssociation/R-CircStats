%global packname  CircStats
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.2_4
Release:          1
Summary:          Circular Statistics, from "Topics in circular Statistics" (2001)
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-4.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-MASS R-boot 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-MASS R-boot

%description
Circular Statistics, from "Topics in circular Statistics" (2001) S. Rao
Jammalamadaka and A. SenGupta, World Scientific.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help