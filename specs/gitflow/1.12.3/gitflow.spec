
%global version 1.12.3
%global arch %(test $(rpm -E%?_arch) = x86_64 && echo "x64" || echo "ia32")
%global srcdir %{_builddir}/gitflow-%{version}

Name:    gitflow
Version: %{version}
Release: 1%{dist}
Summary: Git extensions for Vincent Driessen's branching model.

Group:   Development/Tools
License: LGPL
URL:     https://github.com/petervanderdoes/gitflow-avh

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
outShareHooksDir="${outShareDir}/hooks"

execFiles="git-flow"
scriptFiles="git-flow-init git-flow-feature git-flow-bugfix git-flow-hotfix git-flow-release git-flow-support git-flow-version gitflow-common gitflow-shFlags git-flow-config"
hookFiles="filter-flow-hotfix-finish-tag-message filter-flow-hotfix-start-version filter-flow-release-branch-tag-message filter-flow-release-finish-tag-message filter-flow-release-start-version post-flow-bugfix-delete post-flow-bugfix-finish post-flow-bugfix-publish post-flow-bugfix-pull post-flow-bugfix-start post-flow-bugfix-track post-flow-feature-delete post-flow-feature-finish post-flow-feature-publish post-flow-feature-pull post-flow-feature-start post-flow-feature-track post-flow-hotfix-delete post-flow-hotfix-finish post-flow-hotfix-publish post-flow-hotfix-start post-flow-release-branch post-flow-release-delete post-flow-release-finish post-flow-release-publish post-flow-release-start post-flow-release-track pre-flow-feature-delete pre-flow-feature-finish pre-flow-feature-publish pre-flow-feature-pull pre-flow-feature-start pre-flow-feature-track pre-flow-hotfix-delete pre-flow-hotfix-finish pre-flow-hotfix-publish pre-flow-hotfix-start pre-flow-release-branch pre-flow-release-delete pre-flow-release-finish pre-flow-release-publish pre-flow-release-start pre-flow-release-track"

# Create output dirs
install -v -d -m 0755 "${outBinDir}"
install -v -d -m 0755 "${outShareDir}"
install -v -d -m 0755 "${outShareDocsDir}"
install -v -d -m 0755 "${outShareHooksDir}"

# Exec files
for execFile in $execFiles ; do
	install -v -m 0755 "%{srcdir}/$execFile" "${outBinDir}"
done

# Script files
for scriptFile in $scriptFiles ; do
  install -v -m 0644 "%{srcdir}/$scriptFile" "${outBinDir}"
done

# Hook files
install -d "${outShareHooksDir}"
for hookFile in $hookFiles ; do
  install -v -m 0644 "%{srcdir}/hooks/$hookFile" "${outShareHooksDir}"

# License and contributors
install -d "${outShareDocsDir}"
install -m644 "%{srcdir}/AUTHORS" "${outShareDocsDir}/AUTHORS"
install -m644 "%{srcdir}/LICENSE" "${outShareDocsDir}/LICENSE"
install -m644 "%{srcdir}/README.md" "${outShareDocsDir}/README.md"

%files
%defattr(-,root,root,-)
%doc %{_datarootdir}/gitflow/docs/README.md
%license %{_datarootdir}/gitflow/docs/LICENSE
%{_bindir}/git-flow-init
%{_bindir}/git-flow-feature
%{_bindir}/git-flow-bugfix
%{_bindir}/git-flow-hotfix
%{_bindir}/git-flow-release
%{_bindir}/git-flow-support
%{_bindir}/git-flow-version
%{_bindir}/gitflow-common
%{_bindir}/gitflow-shFlags
%{_bindir}/git-flow-config
%{_datarootdir}/gitflow

%changelog
* Thu Oct 22 2020 Giacomo Furlan <giacomo@giacomofurlan.name> - 1.12.3
- Release 1.12.3
- https://github.com/petervanderdoes/gitflow-avh/releases/tag/1.12.3
* Thu Oct 22 2020 Giacomo Furlan <giacomo@giacomofurlan.name> - 0.4.1
- Release 0.4.1
- https://github.com/nvie/gitflow/releases/tag/0.4.1
