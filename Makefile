PREFIX ?= /usr/local

install:
	mkdir -p "${DESTDIR}/${PREFIX}/bin"             		\
			 "${DESTDIR}/${PREFIX}/share/man/man1"  		\
			 "${DESTDIR}/${PREFIX}/share/tuterm"			\
			 "${DESTDIR}/${PREFIX}/share/tuterm/scripts"
	@# Inject a PREFIX variable definition into the tuterm script
	mkdir -p _build; \
		sed "0,/^PREFIX=.*/s::PREFIX='/${PREFIX}':" tuterm > _build/tuterm
	install -Dm755 _build/tuterm    "${DESTDIR}/${PREFIX}/bin/"
	install -Dm644 docs/tuterm.1     "${DESTDIR}/${PREFIX}/share/man/man1/"
	install -Dm644 config.sh        "${DESTDIR}/${PREFIX}/share/tuterm/"
	install -Dm644 tutorial         "${DESTDIR}/${PREFIX}/share/tuterm/scripts/tuterm"

pacman:
	mkdir -p _build/pacman
	cp PKGBUILD _build/pacman/
	cd _build/pacman; makepkg --skipinteg -f

clean:
	rm -rf _build
