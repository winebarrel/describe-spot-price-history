%define source_url https://bitbucket.org/winebarrel/describe-spot-price-history/raw/6d1ee327a99cfe0dd154aae347b3a8ac330ccc2a/describe-spot-price-history

Summary: describe-spot-price-history
Name: describe-spot-price-history
Version: 0.1.5
Release: 1
License: BSD
 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

Requires: ruby
 
%description
a command line tool for describing the Spot Price history.
 
%install
rm -rf $RPM_BUILD_ROOT
install -d -m755 $RPM_BUILD_ROOT%{_bindir}
curl -s %{source_url} -o $RPM_BUILD_ROOT%{_bindir}/describe-spot-price-history
chmod 755 $RPM_BUILD_ROOT%{_bindir}/describe-spot-price-history
 
%files
%defattr(755,root,root)
%{_bindir}/describe-spot-price-history
