Name:       python3-markdown
Summary:    Python implementation of John Gruber's Markdown
Version:    3.2.1
Release:    1
License:    BSD
URL:        https://pypi.org/project/markdown/
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.bz2
Requires:   python3-base
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
This is a Python implementation of John Gruber's Markdown. It is almost
completely compliant with the reference implementation, though there are
a few known issues. See Features for information on what exactly is
supported and what is not. Additional features are supported by the
Available Extensions.

%package -n markdown
Summary:    Command line tool for Markdown
Requires:   %{name} = %{version}-%{release}

%description -n markdown
%{summary}.

%prep
%setup -q -n %{name}-%{version}/markdown

%build
%{py3_build}

%install
rm -rf %{buildroot}
%{py3_install}

%files
%defattr(-,root,root,-)
%{python3_sitearch}/markdown
%{python3_sitearch}/Markdown-*.egg-info

%files -n markdown
%defattr(-,root,root,-)
%{_bindir}/markdown_py
