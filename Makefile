
install:
	mkdir -p "${DESTDIR}/${PREFIX}/bin"		\
			 "${DESTDIR}/${PREFIX}/man/man1"
	install -Dm755 tuitor "${DESTDIR}/${PREFIX}/bin/"
	install -Dm644 man/tuitor.1 "${DESTDIR}/${PREFIX}/man/man1/"

pacman:
	mkdir -p _build/pacman
	cp PKGBUILD _build/pacman/
	cd _build/pacman; makepkg --skipinteg -f

clean:
	rm -rf _build
