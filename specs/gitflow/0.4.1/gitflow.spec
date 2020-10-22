
%global version 0.4.1
%global arch %(test $(rpm -E%?_arch) = x86_64 && echo "x64" || echo "ia32")
%global srcdir %{_builddir}/gitflow-%{version}

Name:    gitflow
Version: %{version}
Release: 1%{dist}
Summary: Git extensions for Vincent Driessen's branching model.

Group:   Development/Tools
License: LGPL
URL:     https://github.com/nvie/gitflow

BuildRequires: git

Requires: git

%description
A collection of Git extensions to provide high-level repository operations for Vincent Driessen's branching model.

%prep
# Clone the sources
if ! [ -d %{srcdir}/.git ]; then
  git clone %{url}.git %{srcdir}
fi
pushd %{srcdir}
# Reset the git status
  git reset --hard
  git fetch --all
  git checkout %{version}
  git submodule init
  git submodule update
popd

%build
# n/a

%install
# Variables
outBinDir="%{buildroot}%{_bindir}"
outShareDir="%{buildroot}%{_datarootdir}/gitflow"
outShareDocsDir="${outShareDir}/docs"

execFiles="git-flow"
scriptFiles="git-flow-init git-flow-feature git-flow-hotfix git-flow-release git-flow-support git-flow-version gitflow-common gitflow-shFlags"

install -v -d -m 0755 "%{installPrefix}"
# Exec files
for execFile in $execFiles ; do
	install -v -m 0755 "%{srcdir}/$execFile" "${outBinDir}"
done

# Script files
for scriptFile in $scriptFiles ; do
  install -v -m 0644 "%{srcdir}/$scriptFile" "${outBinDir}"
done

# License and contributors
install -d "${outShareDocsDir}"
install -m644 "${srcdir}/AUTHORS" "${outShareDocsDir}/AUTHORS"
install -m644 "${srcdir}/LICENSE" "${outShareDocsDir}/LICENSE"
install -m644 "${srcdir}/README.mdown" "${outShareDocsDir}/README.md"

%files
%defattr(-,root,root,-)
%doc %{_datarootdir}/gitflow/docs/README.md
%license %{_datarootdir}/gitflow/docs/LICENSE
%{_bindir}/git-flow
%{_bindir}/git-flow-init
%{_bindir}/git-flow-feature
%{_bindir}/git-flow-hotfix
%{_bindir}/git-flow-release
%{_bindir}/git-flow-support
%{_bindir}/git-flow-version
%{_bindir}/gitflow-common
%{_bindir}/gitflow-shFlags
%{_datarootdir}/gitflow

%changelog
* Thu Oct 22 2020 Giacomo Furlan <giacomo@giacomofurlan.name> - 0.4.1
- Release 0.4.1
- https://github.com/nvie/gitflow/releases/tag/0.4.1
