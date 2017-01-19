# web/querysets.py
# -*- coding: UTF-8 -*-

from mptt.querysets import TreeQuerySet

class IrUiMenuQuerySet(TreeQuerySet):
    pass

    def split(self, *args, **kwargs):
        pass

        return self.model._tree_manager.get_split_action(self, *args, **kwargs)
