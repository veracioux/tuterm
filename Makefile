
install:
	mkdir -p "${DESTDIR}/${PREFIX}/bin"				\
			 "${DESTDIR}/${PREFIX}/share/man/man1" 	\
			 "${DESTDIR}/${PREFIX}/share/tuterm"
	install -Dm755 tuterm "${DESTDIR}/${PREFIX}/bin/"
	install -Dm644 man/tuterm.1 "${DESTDIR}/${PREFIX}/share/man/man1/"
	install -Dm644 config.sh "${DESTDIR}/${PREFIX}/share/tuterm/"

pacman:
	mkdir -p _build/pacman
	cp PKGBUILD _build/pacman/
	cd _build/pacman; makepkg --skipinteg -f

clean:
	rm -rf _build
