# -*- coding: utf-8 -*-

from invoke import Collection  # pylint: disable=3rd-party-module-not-gated

from . import docs, filemap, gha, loader

ns = Collection()
ns.add_collection(Collection.from_module(docs, name="docs"), name="docs")
ns.add_collection(Collection.from_module(gha, name="gha"), name="gha")
ns.add_collection(Collection.from_module(loader, name="loader"), name="loader")
ns.add_collection(Collection.from_module(filemap, name="filemap"), name="filemap")
