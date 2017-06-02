# -*- coding:utf-8 -*-

import os, math


def calcPhysicalDamage(ctx, srcAttrs, dstAttrs):
    srcAtk = srcAttrs.base.phyAttack
    dstRst = dstAttrs.base.phyResist
    isCritical = _calcCritical(ctx, srcAttrs, dstAttrs)
    if isCritical:
        if srcAttrs.advanced.criticalDamageBoost > 0:
            enhanceFactor = srcAttrs.advanced.criticalDamageBoost / 10000.0
            srcAtk = srcAtk * ctx.consts.PHY_CRITICAL_FACTOR * (1 + enhanceFactor)
        else:
            srcAtk = srcAtk * ctx.consts.PHY_CRITICAL_FACTOR

    dstRst = max(0, dstRst - srcAttrs.advanced.phyPierce)
    resistRatio = dstRst / 10000.0
    dmg = srcAtk * (1.0 - resistRatio)
    dmg -= dstAttrs.advanced.phyAbsorb
    dmg = max(0, int(math.ceil(dmg)))
    return dmg


def _calcCritical(ctx, srcAttrs, dstAttrs):
    criticalRatio = srcAttrs.base.criticalRatio - dstAttrs.advanced.antiCriticalRatio
    if criticalRatio <= 0:
        return False

    return ctx.rnd.rand10000() <= criticalRatio
