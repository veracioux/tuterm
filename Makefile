
install:
	mkdir -p "${DESTDIR}/${PREFIX}/bin"				\
			 "${DESTDIR}/${PREFIX}/share/man/man1" 	\
			 "${DESTDIR}/${PREFIX}/share/tuitor"
	install -Dm755 tuitor "${DESTDIR}/${PREFIX}/bin/"
	install -Dm644 man/tuitor.1 "${DESTDIR}/${PREFIX}/share/man/man1/"
	install -Dm644 config.sh "${DESTDIR}/${PREFIX}/share/tuitor/"

pacman:
	mkdir -p _build/pacman
	cp PKGBUILD _build/pacman/
	cd _build/pacman; makepkg --skipinteg -f

clean:
	rm -rf _build
