# Maintainer: Haris Gušić <harisgusic.dev@gmail.com>
pkgname=tuterm
pkgver=0.0.0
pkgrel=1
pkgdesc="Create and run CLI tutorials/demos/tests easily"
arch=('x86_64')
url="https://github.com/HarisGusic/tuterm"
license=('MIT')
groups=()
depends=()
makedepends=()
checkdepends=()
optdepends=('asciinema')
provides=()
conflicts=()
replaces=()
backup=()
options=()
source=("git+https://github.com/HarisGusic/tuterm")
noextract=()
md5sums=('SKIP')
validpgpkeys=()

package() {
	cd "$srcdir/$pkgname"
	make install PREFIX=/usr DESTDIR="$pkgdir"
}
