# Generated by go2rpm 1
%bcond_without check

# https://github.com/issue9/identicon
%global goipath         github.com/issue9/identicon
Version:                1.0.1

%gometa

%global common_description %{expand:
Go 语言版 identicon 头像产生工具.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Go 语言版 identicon 头像产生工具

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/issue9/assert)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Sun Jan 26 07:01:45 CET 2020 Marcel Metz <mmetz@adrian-broher.net> - 1.0.1-1
- Initial package
