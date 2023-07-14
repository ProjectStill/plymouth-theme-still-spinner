%define set_theme %{_sbindir}/plymouth-set-default-theme
%global branch fragile

Name:           plymouth-theme-still-spinner
Version:        0.9.5
Release:        2%{?dist}
Summary:        stillOS Plymouth Theme
 
License:        GPLv2+
URL:            https://github.com/ProjectStill/plymouth-theme-still-spinner
Source0:        https://github.com/ProjectStill/plymouth-theme-still-spinner/archive/refs/heads/%{branch}.tar.gz#/plymouth-theme-risi-spinner-main.tar.gz

BuildArch:      noarch
Requires:       plymouth-plugin-two-step >= 0.7.0
Requires(post): plymouth-scripts

%description
Plymouth Theme for stillOS

%prep
%autosetup -n plymouth-theme-risi-spinner-main
%build

%install
mkdir -p %{buildroot}%{_datadir}/plymouth/themes/still-spinner
mkdir -p %{buildroot}%{_datadir}/plymouth/themes/still-bgrt
install -m 0644 still-bgrt.plymouth %{buildroot}%{_datadir}/plymouth/themes/still-bgrt
install -m 0644 still-spinner.plymouth *.png %{buildroot}%{_datadir}/plymouth/themes/still-spinner

%post
export LIB=%{_lib}
# on initial install, set this as the new theme
if [ $1 -eq 1 ]; then
    %{set_theme} still-bgrt
fi
 
%postun
export LIB=%{_lib}
# if uninstalling, reset to boring meatless default theme
if [ $1 -eq 0 ]; then
    if [ "$(%{set_theme})" == "still-bgrt" ]; then
        %{set_theme} --reset
    fi
fi
	
%files
%{_datadir}/plymouth/themes/still-bgrt
%{_datadir}/plymouth/themes/still-spinner
	
%changelog
* Thu Aug 19 2021 PizzaLovingNerd - 1.0
- spec file created
