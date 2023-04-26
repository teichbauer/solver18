## 2023-04-25->0.423
- get rid of cluster.block/,pblock
- in the wrong sat with path:
  [(60, 1), (57, 4), (54, 2), (51, 1), (48, 5), (45, 4), (42, 7), (39, 0),    
   (36, 2), (33, 0), (30, 7), (27, 5), (24, 7), (21, 6)]
  there were 4 hits:
  C0068: {12: 0, 18: 1, 37: 0} :H  nov 33
  C0139: {9: 1, 38: 1, 39: 0}  :H  nov 51
  C0181: {3: 0, 34: 1, 47: 1}  :H  nov 54
  C0195: {8: 1, 42: 1, 54: 1}  :H  nov 30
## 2023-04-25->0.422
- docs/20230425-analysisOfblock-dic.txt
- Cluster.layers: an list replacing layer1/layer2
## 2023-04-24->0.421
- BlockChecker.Layer -> BlockChecker.layer
- BlockChecker handles len(dd) == 2 -> filling cvsats]'*'].append(sat)
- cluster.grow_with_filter -> grow_pairs( + pool)
  Cluster.groups: removd
- PathFinder.grow_pairs -> grow_pair_pool
- documents: 20230412-design-tail.txt
  20230422-analysisOfblockcheck-dic.txt
  20230424ov-cvs.txt
## 2023-04-21->0.420
- clean up
## 2023-04-20->0.419
- for COMBOn vk, add okname containing the old 2 knames
- cluster grow_layercv: handle lyr_filter better
## 2023-04-19->0.418
- add layer.grid_sat to cluster.sat
## 2023-04-18->0.417
- saved all in solver18-416
- clear up a bit. 
- Center.tailbits, and cluster.headsatbits
## 2023-04-18->0.416
- fix a bug in cluster:194
- add print-outs in pathfinder, for analysis
- reached pathfinder.collect_sats for a bottom cluster named:
  [(60, 1), (57, 4), (54, 2), (51, 1), (48, 5), (45, 4), (42, 7), (39, 0), 
   (36, 2), (33, 0), (30, 7), (27, 5), (24, 7), (21, 6)]
## 2023-04-17->0.415
- some tracing when finding path.
- printouts saved in 412-20230415-paths.txt
  till cluster:[(60, 1), (57, 3), (54, 0), (51, 3), (48, 7)]-[[5]]
## 2023-04-17->0.414
- refactored cluster, to set cluster.sat occluding 
  lyr.vk2dic, generating new sat, or, if a vk has 2 bits in sat,
  gets hit, so that its cvs will be dropped out od the path.
## 2023-04-16->0.413
- new: cluster.set_satfilter, finding cluster.sat touching
  lyr's bidic that can be sat-hit, or drop kn, or new sat.
## 2023-04-16->0.412
- prpgress in pathfinder.py
- fix in cluster.py
- gone thru 60.1+57.1, 60.1+57.2. 
  in 60.1+57.3 - 51.2 - 48.6, a bug hits ->fixed now
## 2023-04-14->0.411
- refactoring in cluster
- pahfinder/search: depth-first search progress
## 2023-04-13->0.410
- progress in cluster, pathfinder
## 2023-04-11->0.409
- center: vk2pairs, vk2dic, .add_vk2
- clause.bits reverse sorted
- cluster: progress
## 2023-04-10->0.408
- complete 407 changes
- cluster.grow_cvsats: setup cluster.cvsats
## 2023-04-10->0.407
- tail -> layer
## 2023-04-03->0.406
- tail: no more n2sat_dic .generate_n2s()
- no n2sat_dic in satnode for making tail
- pathfinder: refactor grow_pairs
- cluster: progress
## 2023-04-02->0.405
- cluster.grow_with_filter
- PathFinder.grow_pairs using cluster.grow_with_filter
## 2023-04-01->0.404
- get rid of branch, Center.tails = {} replace Center.root_branch
- clean up tail a bit
- pathfinder.grow_pairs to replace .grow
- BlockChecker.block_refs
## 2023-04-01->0.403
- tail.cvsats={}, filled by tail.bchecker of type BlockerChecker
- BlockChecker.make_cvsats: transfer dat in checkdic to tail.cvsats
## 2023-03-30->0.402
- solver18
## 2023-03-30->0.401
- understood what I previously did in tail.bchecker and .blbmgr.
  wrote this info into docs/0398-blockers-a.txt /0400-tail-vks.txt
  After this check-in, I will branch off to be solver18.
## 2023-03-26->0.400
- 0398-blockers-a.txt: try to under stand
  tail. bchecker/block_dic, checkerdic
      .blbmgr.block_bv_dic, cbdic
## 2023-03-25->0.399
- preparing for more sat-analysis
  basics: test_clauses, sat_compatible
  Center.test_clauses (test against know 8 sats)
- refactor pathfinder
## 2023-03-24->0.398
- satx8: list all 8 sats, with 14x4 head-sats and 18 body sats
- pathfinder/cluster block_filter, pblock_filter, remove_clause
## 2023-03-21->0.397
- progress
## 2023-03-20->0.396
- pathfinder/cluster/blocker getting ready for set-pblock
## 2023-03-20->0.395
- fixes in pathfinder/downwards
- rename cluster.bsatbits to .headsatbits, other refactoring in cluster
- clause: added mark = (nov, (cvs))
- minor changes in pathnode
- progress in pathfinder
## 2023-03-16->0.394
- block.py new class for cluster.block
- cluster constructor support clone, cluster.merge_cluster
- pathfinder.downward_blocker removed.
## 2023-03-13->0.393
- in cluster.py: self.tail1/tail2, blocker_set, test_sat
- in pathfinder.py: downwards
## 2023-03-11->0.392
- PathFinder.downwars
- progress in cluster
## 2023-03-10->0.391
- got rid of layer.py, vk2pkg.py
- new: cluster.py
- pathfinder: calc 60-57, 54-51, 48-45, 42-39, 36-33, 30-27, 24-21
  each will have 49 merged clusters
- recoded pathnode/add_k2
## 2023-02-25->0.390
- fixes in cvnode2
- progress in pathfinder/down_blocker
## 2023-02-23->0.389
- bitgrid: new method: bv2cvs
- Center.bodybits renamed to headbits, it is now a dict of {<nov>:{bits},..}
- CNNode2: self.lower_blocks set{}
- fixes in path
- pathfinder/downward_blocker set all cvnode2 for dowward-blocks, if it 
  has sat, and bit(s) in sat sit on lower tail's head
- pathnode/add_k2 now takes just vk/cl, no more kname and dic
- clause (k2) name ->kname, to be compatible with vklause
- millipede: some progress
## 2023-02-22->0.388
- new: path.py, pathnode.py, pathfinder.py, millipede.py
## 2023-02-20->0.387
- remove pathseg.py new: millipede.py
- new PathNode class, both CVNode2 and Path inheriting from it
- new: bitgrid.cv_sats
## 2023-02-15->0.386
- new: cvnode2.py - class CVNode2
- satnode: when constructing tail, collect sats and feed it to tail.node2s
## 2023-01-27->0.385
- progress
## 2023-01-23->0.384
- add method .evaluate_overlap to Clause, and other updates there
- node2sat.add_clause: not yet done
- other changes in layer, and pathfinder, lib2
## 2023-01-14->0.383
- progress
## 2023-01-14->0.382
- layer.py
## 2023-01-09->0.381
- refactor and fixes.
## 2023-01-05->0.380
- take from solver16 -> solver17
- 2sat: solve 2sat with backtracking in 2sat/solve2.py
## 2022-12-26->0.379
- clean up some
- turn it to be solver17
## 2022-10-29->0.378
- optimization in pathseg
- in levelpath.verified_add_pseg, (line71) tried to cover a case 
  elif psg.vkname == bdic['kn']:
      if psg.dic == pseg.dic:
  it is not yet clear.
## 2022-10-27->0.377
- more mending in pathseg
## 2022-10-27->0.376
- fix in pathseg
## 2022-10-27->0.375
- run till nov-39's vks. Done halfway:
  C0227,C0008,C0123,C0012,C0106,C0002. To yet check:
  C0204,C0101,C0125,C0167,C0014,C0177
## 2022-10-24->0.374
- progress in pathseg.py
## 2022-10-20->0.373
- in case of a pseg.bvdic: {50:0}:30(123)^24(045), and
  vk(39)[50-1,24-0](vk.cvs)
  if bv(50)==0, pseg is blocking already, so bv(50) can only be 1, and
  in this case vk(39) with bv(50==1), will result in block-bv(24)==0.
  So, in case vk(39) with a bv(bit) where bit is in pseg.bvdic, and
  pseg.bvdic[bit] != vk(39).dic[bit], here vk will turn to become a
  blocker-pseg, with bvdic {24:0}.
  In <= 0.372, this test was "pseg.bvdic[bit] == vk(39).dic[bit]", this
  needs to be reversed to "pseg.bvdic[bit] != vk(39).dic[bit]", then
  vk(39) turns to become a pseg.bvdic += {24:0}, or a 
  new pseg with {24:0}.
  And in case of "pseg.bvdic[bit] == vk(39).dic[bit]", vk is 
  to be skipped.
## 2022-10-20->0.372
- for the case both bits of a vk(vb1,vb2) are hit by a blocker-pseg(pb1,pb2):
  (in pathseg.filter_vk where len(bs) == 2)
  1. if val(vb1)==val(pb1) and val(vb2)==val(pb2):
     vk is covered by pseg: vk-b1 covered by ps-b1m so vk becomes a 1 bit 
     blocker. And this 1-bit blocker is again covered by pseg. so vk is covered
  2. if val(vb1)!=val(pb1) and val(vb2)!=val(pb2):
     vk is not needed because its hit-case will never happen
  3. if val(vb1) != val(pb1) and val(vb2)==val(pb2):
     va(vb2) makes vk become 1 bit blocker with vb1, but then, this blocker is
     in conflict with pseg's blocking range. So
     pseg.blocker[port][vk.nov] = vk.cvs
## 2022-10-18->0.371
- progress at levelpath-grow:39-36
## 2022-10-11->0.370
- modified in pathseg.py and levelpath.py
## 2022-10-10->0.369
- progress in pathseg and levelpath
## 2022-10-08->0.368
- progress in levelpath and pathseg
## 2022-10-04->0.367
- progress in levelpath and pathseg
- fix in klause.py/clone
## 2022-09-29->0.366
- refactoring levelpath and pathseg
## 2022-09-28->0.365
minor fix in pathseg: add new blocker in filter_vk
## 2022-09-26->0.364
- rename levelnode -> levelpath
- new: PathSeg
## 2022-09-21->0.363
- progress in levelnode
## 2022-09-20->0.362
- levelnode for pathketten : a bundle of all path on a nov level
## 2022-09-16->0.362
- the standing-alone blockers, as in nov60: 24:{1:{1,3}}, 9:{0:{3,7}}, and
  also the from them derived stand-alone blocker as in nov57: 30:{0:{5}} and
  nov54 36:{1:{2}}.. are added to tail.bchecker.checkdic in 
  blbmgr.add_block_bv_dic, so the BlockChecker.merge_blbmgr_blocks is no 
  longer needed.
- center: added: blocker_dic/cblocker_dic, and a cls method: add_blocks
  for collecting all across novs
## 2022-09-12->0.361
- start coding Center / add_blocks
## 2022-09-12->0.360
- changed formats of bchecker.checkdic: 
  build_checkdic      -> build_checkdic1, 
  merge_blbmgr_blocks -> merge_blbmgr_blocks1
## 2022-09-10->0.359
- after bchecker.build_checkdic() call, new: bchecker.merge_blbmgr_blocks for
  merge tail.blbmgr.blobk_bv_dic to bchecker.block_dic
## 2022-09-09->0.358
- fixes in blockchecker, and in blbmgr
## 2022-09-08->0.357
- BlockChecker/build_checkdic now handles the case of:
  nov54 [55 15  3](7)
    51: 'C0108': ({2, 4, 6}, {0, 2, 4, 6}, (46, 1))
        'C0109': ({1, 4, 5}, {0, 1, 2, 3}, (19, 0))
    ...
    27: 'C0192': ({1, 3, 5, 7}, {0, 1, 2, 3}, (11, 1))
        'C0010': ({1,3}, {2, 3, 6}, None)
        'C0084': ({1, 2, 3}, {4, 5, 6}, (42, 1))
  this None-case will ends up with a bchecker.block_dic entry:
    '*': {54: (2,3,6), 27:(1,3))}
- blbmgr/cbdic_oppo for handling the case like:
  nov51 [39 20  9](0)
    48: 'C0165': ({2, 3, 6, 7}, {4, 5, 6, 7}, (44, 1))
    ...
    39: 'C0217': ({0, 1, 4, 5}, {2, 4, 6}, (43, 0))
        'C0013': ({0, 1, 4, 5}, {2, 3, 6, 7}, (19, 1))
        'C0198': ({0, 2, 4, 6}, {4}, (26, 1))
        'C0033': ({0, 2, 4, 6}, {3, 7}, (19, 0))
  where (19,0) conflicts with (19,1). Now this leads to a block_dic entry:
    '*':{51:(3,7), 39:(0,4)} - these path will not be picked as sat-path
## 2022-09-07->0.356
- fix a bug in bitgrid/bits_cvs: when input dic has 2 two bits, wrong 
  returned cvs
- tail will have its bchecker setup(as empty) in tail-contructor. And
  snode will call tail.bchecker.build_checkdic()
- remove  build_checkdic() call from blockchecker-constructor
## 2022-09-06->0.355
- blockchecker
- 0353-blockers.txt, 0354-blockers.txt
## 2022-09-04->0.354
- blockchecker
- modified: pathketten/blocks_from_cbdic
## 2022-08-25->0.353
- fix in pathfinder, pathketten, vk2pkg
## 2022-08-24->0.352
- complete pathfinder/search_path
- complete pathketten
- vk2pkg coding
## 2022-08-23->0.351
- progress in vk2pkg and pathketten
## 2022-08-22->0.350
- new: pathketten
- modified: pathfinder
- Vk2pkg
## 2022-08-19->0.349
- progress in pathfinder
## 2022-08-19->0.348
- progress in pathfinder
## 2022-08-18->0.347
- snode>Center.bodybits : set of bits coing from all bgrids
- progress in pathfinder
## 2022-08-17->0.346
- get rid of sat2, and snodevkm
- new: pathfinder.py
## 2022-08-16->0.345
- fix blbmgr.add_cbd
- minor update tail
- branch: sumbdic keeps lists of vks under each bit. every vk has 
  nov in it
- snode.heads_schwanz shows nof  head-vks/nof schwanz-vk
## 2022-08-16->0.344
 - intro blbmgr.cbdic for conditional partial-/total-blockers
## 2022-08-12->0.343
- got rid of vk12mgr
## 2022-08-08->0.342
- split_sats moved from blbmgr to tail
- blbmgr.block_sat refactored
- regardless a sat-bit in tail.bdic or not, that tail will be cloned.
## 2022-08-07->0.341
- blbmgr.block_sat for handling the case: sat-bit hit a block-bit
- tail.remove_kn2_from_cvk_dic handles the case where cv not existing
## 2022-08-07->0.340
- refactored tail, blbmgr and branch
## 2022-08-06->0.339
- blbmgr.add_split_sat stubbed
## 2022-08-06->0.338
- new 0337-info.txt for blbmaps and more before split/clone.
## 2022-08-06->0.337
- fixing / completing 0.336 in tail
## 2022-08-05->0.336
- chang satmgr to blbmgr. sat_cvs_dic to block_bv_dic, now no more saving the
  sat under a bit, but the cvs being blocked by the bv under this bit.
  This make it logically easier to be fathomable
## 2022-08-02->0.335
- progress
## 2022-08-02->0.334
- polishing/fixes in satmgr, tail
- doc: display chain before split -> docs/0333.info.txt
## 2022-08-02->0.333
- finished tail.eval_combos - if a new combo-vk2 has any bit overlapping with
  satmgr.sat_cvs_dic bit, evaluate it.
## 2022-08-01->0.332
- combon vk2 can have cvs that some sats in tail.satmgr.sat_cvs_dic cover
  and this may generate new sat, or reduce cvs in the combo-vk2.cvs
  In progress to deal this - in tail. Not yest finished.
## 2022-07-30->0.331
- tail.combos[] for the case: vka/vkb with the smae dic
- handle vka/vkb with the same bits, but resulting a new sat(1 value differs)
## 2022-07-28->0.330
- progressing
## 2022-07-23->0.329
- refavtored branch
- center.root_branch
- refactored tail, modified snode
- in stead of picking teh bit of most vk2s, pick least used bit
## 2022-07-22->0.328
- refactored branch
- root_branch under Center
## 2022-07-21->0.327
- snode, tail displaying info
## 2022-07-21->0.326
- refactored bmap:{bit: [(cvs, sat),(cvs,sat)], bit:[]} to
  sat_cvs_dic: {bit: {0:cvs, 1:cvs}, bit: {},...}
- vklause sat1() turning a vk1 to a sat-pair (bit, value)
- remove basic/vk1_to_sat
## 2022-07-20->0.325
- refactored satmgr.add, removed clone
- tail: remove_kn2_from_cvk_dic, copy_bdic, copy_cvks_dic. refactored clone
- vklause.clone now copies cvs(set) to the clone, if no delta is given.
## 2022-07-19->0.324
- more implementations in branch
- center.get_tailchain
- some fixes in satmgr
- tail: remove_vk2, clone
## 2022-07-19->0.323
- satmge.clone, tail.clone
## 2022-07-18->0.322
- tail.vk12dic renamed to be vk2dic
## 2022-07-18->0.321
- refactored satmgr.py. It worked all hte way till snode.nov == 21
  the branch/split should start
## 2022-07-17->0.320
- refactored tail.py
- new: branch.py
- get rid of center.sumvk12dic, .solve(), get_maxes -> get_maxbit
- no more kss in tail-contructor/snode
## 2022-07-15->0.319
- refactor tail
- center.vk2bdic for choosing bit for split
## 2022-07-12->0.318
- refactored tail, satmgr. finished tail setups for all sn(50-21)
- draw a bit map for every sn in 0318-info.txt
## 2022-07-08->0.317
- refactoring tail. Not yet tested.
## 2022-07-08->0.316
- fixes in tail.py
## 2022-07-08->0.315
- fixes in tail.py
## 2022-07-07->0.314
- new class: SatManager
- on a cv, say cv==3, when the bits from sats overlap with a vk2's bit, making
  the vk2 become a vk1, on that overlapped bit, if 
  vk2.dic[bit] != sat[bit], e.G. sat:{24:0}, and C0073{24:1, 12:1}, so that
  C0073.dic[24] != sat[24], this means, this sat makes C0073 True(non-hit)
  already, so C0073 can be absent in cvks_dic[3].
  If C0073a is {24:0, 12:1}, then C0073a.dic[24] == sat[24] (==0), then,
  C0073a's 24:0 is a duplicate of sat, and can be removd, it will turn to a
  vk1 {12:1}, and a new sats={12:0} will be added to SatMgr
## 2022-07-06->0.313
- tested until new_bmap = {}. docs/0312-info.txt
- issue: self.sbmap not being updated along the way
## 2022-07-05->0.312
- first complete version of Tail
## 2022-07-05->0.311
- new progress in tail.py
## 2022-07-04->0.310
- design of Tail: on going
## 2022-07-03->0.309
- progress in Tail
## 2022-06-29->0.308
- new version of Tail class. Yet to be completed
## 2022-06-27->0.307
- class Tail replacing S2
## 2022-04-29->0.306
- putting to GitHab
## 2022-04-13->0.305
- fix in snodevkm.add_vk1
## 2022-04-13->0.304
- fixes in snodevkm
## 2022-04-12->0.303
- fixing snodevkm
- add snodevkm.bitdic/.kn1s/.kn2s Now for debugging, may be removed later.
-- sat2.chvkdic{v, <set>}
## 2022-04-11->0.302
- mrtge vk12mgr into snodevkm. sat2 and snodevkm share bdic, chvkdic
## 2022-04-09->0.301
- remove cnode
- vklause.cvs is now set, no more list
- clean up bitgrid/reduce_cvs, get_vk12bits, find_blocks. 
  simplify cvs_and_outdic.
- add snodevkm/add_duplicate, add_dupbits_compliment
## 2022-04-08->0.300
- progress. TBD: VK12Manager.add_vk2/pair case
## 2022-04-06->0.299
- progress
## 2022-03-15->0.298
- vk12m: when adding a new vk resulting a vk dropping its bit(s), there will be
  a new vk generated and added. So that the original vk remains not-altered.
- other progress.
## 2022-03-05->0.297
- with CNode / blocks,  the performance is bad (waited for 5 min, still running)
- bottom up from last_nov's snode: Center.sat_pathup
## 2022-03-01->0.296
- progressing on CNode
  60.1-57.0-54(0,4): 54.0-51.5-48(1,3,5,7) -> 45.3
  60.1-57.0-54.0-51.5 has no end: this should remove 51.5 -> remove54.0
  it should turn to 54.4
## 2022-02-28->0.295
- progreeing on cnode and satnode
## 2022-02-28->0.294
- Center.set_satbits, that:
  set front_kns (vks in a child-vkm, with oth of its bits in satbits);
  tail_kns(vks with both of its bits in tail-bits(not-satbits)); and
  tailpart_kns(vks with at least 1 bit in tail-bits)
- Center.set_lower_snodes setting snode's snodes-list(descending in nov) with lower
  nov than snode.nov
## 2022-02-20->0.293
- branching off solver15: solver13 was 2.5 secs, faster than solver15(4secs)
  that's because in solver15, I add all vk12s to every pvname/vkm12.
  I want to explore here in solver16, only using v the vk12s from child-vk12m,
  that are overlapping with th3e following snode's bgrids.
  I jope I can reach less than 2 secs performance with this approach.
## 2022-02-19->0.292
- cleaning up: delete tnode, node2
- solve 266/60 (cfg60-266.json) using 4 secs. finding 8 sats
## 2022-02-18->0.291
- designing satnode/solve
## 2022-02-16->0.290
- fixing in satnode and bitgrid
- vk12m/add_vk's return T/F is not validity, but is added or not.
## 2022-02-16->0.289
- redesigned / refactored
## 2022-02-10->0.288
- refactor snode.chdic
## 2022-02-03->0.287
- taking over solver14
## 2021-10-17->0.286
- snode.vk12dics keeps every chheads/v, if there is no vk12, then as {}
  so that 1 node2 cwill be made for this.
- node2 progress
## 2021-10-14->0.285
- fix a bug in vkm.make_choice - pop vk didn't clean vk's bits in bdic.
  also, when using pop_vk(kn), clean up bdic[bit] if it becomes empty.
## 2021-10-13->0.284
- simplify satnode.__init__/.split_vkm
## 2021-10-12->0.283
- node2.verify_vk1: check 2 node2's vk1ms are in conflict
- split-bit is moved to node2, from vk12m
## 2021-10-12->0.282
- vk12m.pick_sbit: sbit only has overlapping kn2s
- progress on node2.merge_node2, usage env in snode.
## 2021-10-11->0.281
- fix vk12m.valid setting bug: it is set to be True by default.
- got rid of twos in node2
- node2 vkm is now kept, not popped empty when spawn.
- snode: n2 construction moved higher level - hope to use node2 on all levels.
## 2021-10-10->0.280
- vk12m.valid fix
## 2021-10-08->0.270
- fix bugs brought in by 0.269
## 2021-10-08->0.269
- understand why in node2.verify_merge, a kn in n2 can be in vkm from n2's 
  parent-snode.
## 2021-10-01->0.268
- node2/verify_merge returns a dict keyed by indexes.
- satnode/spawn: tnode-name pattern: 54.0-(57.a-60-b)(index)
- tnode counts:
  54
  old 54.0:42  54.1:34  54.2:16  54.3:30  54.4:23  54.5:36  54.6:9
  new 54.0:58  54.1:42  54.2:21  54.3:22  54.4:45  54.5:18  54.6:2

  51
  old 51.1:55  51.2:41  51.3:81  51.4:0  51.5:45  51.6:21  51.7:37
  new 51.1:7   51.2:0   51.3:0   51.4:0  51.5:18  51.6:0   51.7:0
- issue: all 4 sat-paths are with
  1: ..51.2-54.1-57.7-60.2
  2: ..51.2-54.1-57.7-60.2
  3: ..51.2-54.1-57.7-60.2
  4: ..51.2-54.1-57.7-60.2
  but now 51.2:0 ? something is wrong.
## 2021-10-01->0.267
- fix in node2/verify_merge: adding failed doesn't mean vkm is invalid!
- satnode: handle gvkms index as part of tname.
## 2021-09-28->0.266
- progress in node2
## 2021-09-28->0.265
- add-up vk1s to the end-nodes, and collect these end-nodes in root
  get rid of sats collection
## 2021-09-24->0.264
- node2 tree starts working, collecting sats.
## 2021-09-23->0.263
- progress in node2
## 2021-09-21->0.262
- progress in node2
## 2021-09-20->0.261
- node2.parent
## 2021-09-19->0.260
- node2 progress
- fix vk12m/remove_vk1
## 2021-09-19->0.259
- fixing/polishing node2
## 2021-09-17->0.258
- trial with node2
- fix VK12Mgr/remove_vk1
## 2021-09-14->0.257
- fix in vk12mgr/add_vk1
## 2021-09-10->0.256
- progress on analyzing tn.grp logics
## 2021-09-07->0.255
- branch off solver14 from solver13. solver13 now performs better:
  cfg60-266.json can be done in 1.2sec in stead of 1.7sec. But now use
  solver14 to explore more possibility.
## 2021-09-05->0.254
- Center/satbits and .bits update moved to split_vkm
- get rid of vk12mgr/bset
- make sure vkm.bdic desnt have empty list (remove entry if)
## 2021-09-04->0.253
- move bit-grid/tn_grps to tnode/get_grps.
- snode calling of tn_grps updated
## 2021-09-04->0.252
- progress
## 2021-09-03->0.251
- progress
## 2021-09-02->0.250
- new method BitGrid.hit to test if a sat-dic is hit by one of the avks of 
  this bitgrid
- tnode/get_sats update
- now cfg60-266.json performs better: 1.2sec (from 1.72sec)
## 2021-08-31->0.249
- snode no more saves choice: save avks, bits, cvs in bgrid, save self.touched
- tnode/get_sats calling .get_rsat and .get_nsat 
- new: Center.bits, Center.satbits
- vk12m.clone offers deep/shallow clone
- vklause.hbit_value modified to return b/v pair of the hight-bit
## 2021-08-29->0.248
- tested 0.248
- tnode.get_sats set-up
## 2021-08-29->0.247
- get rid of snode.done. .next == None means the same
- there is an issue on sn.24, where its vk2grps only has (as ch-value key)
  {2:..,3:..,7:..}. But it parent sn.27 has 4 tnodes, with tnode.grps = {5:..}
  with previous snode.spawn, the outer loop run thru self.vk2grps, here the 5
  will not hit, so resulting no child-tnode.
  Now, for the semantics of snode.vk2grsps: if it misses a ch-value (as in 
  self.bgrid/chheads), doesn't mean this value is not yielding, but rather in 
  the opposite: this value has no restrictive vk2 for it.
  So I should loop thru bgrid.chheadsm, not vk2grps
## 2021-08-26->0.246
- tested BitGrid/tn_grps0 with new coding: it has the same output as tn_grps
  replace tn_grps with it.
- vklause has a new method: .equals
## 2021-08-26->0.245
- add bitset in BitGrid - simplifying set-intersection calls
- fix missing of popping avks from choice, get rid of next_choice, is_top
- vkmgr: choose_anchor -> make_choice, pop avks from vkdic into choice['avks']
## 2021-08-25->0.244
- get rid of PathManager class and pathngr.py
- get rid of tnode/approve
- shorten vk.compressed_value to cmprssd_value
- testing bitgrid/tn_grps0
## 2021-08-24->0.243
- fix in snode.
- minor change in vk12mgr
- polishing names in bitgrid
## 2021-08-23->0.242
- progress
## 2021-08-23->0.241
- testing snode/spawn and more
## 2021-08-21->0.240
- fix bitgrid/find_vkgrps
## 2021-08-21->0.239
- coding bitgrid/find_vkgrps
## 2021-08-21->0.238
- progress
## 2021-08-21->0.237
- progress
## 2021-08-20->0.236
- progress on snode, bitgrid and tnode
## 2021-08-18->0.235
- split-vkm for every snode down to the one snote with vkm length==0
  now every snode has its bitgrid, grps.
- TBD: snode.solve.
## 2021-08-13->0.234
- Center now outputs path-info.json comparable with that from solver12.
## 2021-08-13->0.233
- diagnostic tool in center: saves path-info.json. I already saved that of 
  solver12. Now I can compare, to analize what is going on.
## 2021-07-25->0.232
- progress in vkmgr/morph
- fix in tnode
## 2021-07-25->0.231
- progress in vkmgr/morph
- optimized bitgrid and satnode: bvks and chheads are now tuples, 
  no more list/sets
## 2021-07-23->0.230
- progress in vkmgr/morph
## 2021-07-21->0.229
- update vkmgr
## 2021-07-21->0.228
- progress on snode, tnode, vk12mgr, vkmgr/morph
## 2021-07-19->0.227
- remove nov from vklause, vkmgr and vk12mgr
- progress in satnode, vkmgr
## 2021-07-16->0.226
- fix in bitgrid in case outdic has all the bit of vk.
- progress in vkmgr, tnode 
## 2021-07-14->0.225
- fix in bitgrid.cvs_and_outdic
- tnode.approve
- vkmgr.morph: in case snode.parent exists, use tnode.approve
## 2021-07-13->0.224
- bitgrid: when out_dic empty, now cover the case vk.nob < 3: return a 
  list of covered values (if vk.nob == 3, returns a single cover-value)
- progress in vkmgr and tnode.approve
## 2021-07-12->0.223
- progress
## 2021-07-10->0.222
- new BitGrid class
- vkmgr.morph now uses snode.bitgrid
- satholder.reduce_vk replaced by snode.bitgrid
## 2021-07-06->0.221
- solver13 branched off from solver12
## 2021-06-25->0.220
- Center.skeleton/topdowns for re-structuring the way of finding paths.
## 2021-06-15->0.219
- cfg60-280.json triggers a bug:
  File "solver12.py", line 30, in process
      while not sn.done:
  AttributeError: 'NoneType' object has no attribute 'done'
- solved. In cfg60-280.json, when sn.nov == 30, there exists no path. This 
  should make sn.done to True. And Center.sats[] is empty.
## 2021-06-15->0.218
- when a sat has value 2(allowing both 0 and 1): 
  1. vklause.hit covers that; 2. showing 2**(cnt) as sat count.
  this way, cfg60-266.json has 4x 2 -> 8 sats
## 2021-06-14->0.217
- cfg60-266.json now finds only 4 sats? new bug(s) introduced?
  no. inthese 4 sats, 26:2 is a double. So I did get all 8 sats.
## 2021-06-12->0.216
- cfg12-55.json - node2, works now
## 2021-06-11->0.215
- node2.spawn replace reduce.
## 2021-06-07->0.214
- node2 starts working
## 2021-06-05->0.213
- recode node2/reduce, set_bvk
## 2021-06-04->0.212
- redesign node2/set_bvk - not yet finished.
## 2021-06-02->0.211
- node2/reduce progress
## 2021-05-26->0.210
- progress: node2 now has sh.
## 2021-05-25->0.209
- progress
## 2021-05-20->0.208
- Node2 for processing vks in vkm. Not yet finished.
- get rid of node12.
## 2021-05-19->0.207
- add_ancvks?
## 2021-05-15->0.206
- cfg60-266 found all 8 sats correctly using 1.746 secs, compared to 26+ secs   
  using solver4, it is big progress. I will do some more optimizations later.
## 2021-05-14->0.205
- move maxnov from SatNode to Center
- recoding pathmgr/finalize:
  -- all vk1: sat just has the opposite value as vk1.dic[bit]
  -- every path-name (12.4 -> 12, 4) in path will set 3 bit/vals
  -- all free bits will varry 0/1
  -- all vk2 : TBD
## 2021-05-12->0.204
- found a bug!
  60.2/vmk has a vk:C0051{8:1, 9:0}. 50.2/hsat:{39"0,20:1,9:0} reduced it
  to C0051{8:1}. All the steps till here are okay. But, when 30.5/vkm.vkdic=={},
  with 30.5/hsat{59:1, 42:0,8:1}, C0051.partial_hit_residue(hsat) should
  return total_hit==True. But I did a direct assignment pvkm = vkm, without
  doing C0051.partial_hit_residue(hsat) check.
  fix: now regardless if self.vkm is empty or not, always do 
  pvkm = self.vkm.clone(), then loop thru every vk in path-vkm, checking with
  hsat. In this case C0051 will generate a total-hit, which would block this
  30.5-33.2-36.6-39.7-42.7-45.5-48.6-51.2-54.1-60.2
## 2021-05-07->0.203
- new
## 2021-04-22->0.202
- center for holding repositories: moving snodes, anchor_vks from SatNode,
  repo from TNode, and sats from PathManager.
## 2021-04-16->0.201
- SatNode offers a class var, collecting all anchor-vks, keyed by nov
- tnode has a add_ancvks to use SatNode.anchor_vks
- vklause.clone offers an option to drop bit
- rename vkmgr/bestchoice to make_choice, bestkey -> ancs
## 2021-04-12->0.200
- simplifying: list(sorted(list(d.keys()), reverse=True)) simplified to be:
  sorted(d.keys(), reverse=True), in many places.
- every snode's bvk clause(s) as in nov-60:C0141/C234: {16:0,6:0,1:0} and
  {16:1,6:0,1:1}, and all from other snodes(nov-57,...nov-24). These dics
  should be used in pathManager, when adding vks into tn.pthmgr.dic?
  Need to be careful, and testing while implementing...
  Added SatNode.anchor_dics=[{},{},..], preparing.
## 2021-04-10->0.199
- changes in vkmgr
- change in node12: vkm assigned always
- SatNode has a class var snodes for debugging purpose. update_cnt. 
  remove conclude
- refactored tnode.
## 2021-04-08->0.198
- fix in snode.trim_chs
- cfg60-266 reached nov21, when there is only 1 vk3 (C0225{54:0, 50:0, 11:1}),
  and now I have to treat this case: stop in vkm.morph, snode.conclude(): TBD.
- there seem to be more paths/tnodes than there should be - trim_chs needs some
  rework?
## 2021-04-07->0.197
- a tough fix in vk12m,add_vk1: kns is a clone of the list from bdic.
  But in the for kn in kns loop, this list may have been updated, so that
  the loop var kn be no more in this list. If that happens: jump over it.
  Did a similar fix for add_vk2 - a cautious check.
## 2021-04-06->0.196
- simplify node12: remove .nov, .val
## 2021-04-06->0.195
- minor change in node12
## 2021-04-06->0.194
- get rid of restrict
- clean up satholder, of many unused methods
- clean up basics of many unused functions
- clean up pathmanager of unused methods: verify_paths, extend_vkm
- node12.collect_sat: when it has hsat of length 3, it is a duplicate of its
  tnode-parent. Dont collect that, it will be collected in tnode-loop.
- minor fix in vk12m
## 2021-04-05->0.193
- delete TransKlauseEngine
- recode node12.check_done. TBD: node12.collect_sat 
## 2021-04-05->0.192
- minor fix in tnode.filter_paths
- node12.spawn: not using tx any more. use sh.reduce
- vk12mgr: pick_bvk: just pick first vk1, if exists, or first vk2
  since there is no tx to be done any more.
- vk12m.morph recoding - need more testing.
## 2021-04-04->0.191
- fix in tnode
## 2021-04-03->0.190
- minor fix in vklause
- recode pathmgr constructor for case when parent isn't top level
- tnode.filter_path, will replace find_path_vk12m and pathmgr.extend_vkm
## 2021-04-03->0.189
- refactored tnode.check_sat - it 1.check if sdic is blocked by local vkdic, and
  2. if not blocked, filter out some vk from vkdic, return the residue vkdic.
  tnode.find_path_vk12m now has input vkdic. no more need bmap
- vklause.partial_hit_residue modified: no more need bit_txmap, and now also
  covers total hit(blocking hit)
- clean up vkmgr a bit
- pathmanager constructor: changed case when parent is top-level.
## 2021-04-02->0.188
- fix in vkgrm. old 12.2->12.4,12.3->12.5,12.4->12.2, 12.5->12.3
  9.2->9.1,9.1->9.2,9.5->9.6,9.6->9.5
  But all vkm.vk12dic are fine(the same as before)
- TBD: what snode.nov, vkmgr.nov now should mean? Because all vks now arenever 
  shortened?
## 2021-04-02->0.187
- refactor vk12m.add_vk, info more complete.
## 2021-04-02->0.186
- solver11 -> solver12
- satholder.reduce make .next_sh, and shorten sh to be 3 loog 
- satholder.reduce_vk: impl of basics.topbits_coverages.
- vklause.cmprssd_value return the nob-long bits, arranging dic to fill in 
  [0,1,2] for nob==3, and [0,1] for nob==2, the  binary value. example:
  {8:0,3:1,0:1} -> 011(3), {21:1,3:0,1:1}->101(5), {4:1,2:0}->10(2)
  this will be the cvr for the bvk vks.
- satnode: remove topbits, usage of tx
- vkmgr.morph: recode morph. Not yet finished.
## 2021-04-02->0.185
- branch off solver12, from solver11(0.184)
  It became complex on hsat/sh management and overview. It is bug-prone. I am 
  now thinking to not tx the bit-position for the variables at all. 
  The consequences:
  * the meaning of "top" (in top-bits) is now symbolic, not real.
  * the vk12s will drop the top bits, in stead of tx/cut top bits, so that their 
    bits, if in the top-bits: dropped, if not in top-bits, kept. And nov will be
    cut by 3.
  * snode keeps tx, and its sh will keep the positions of the 3 top-bits
  * children of snode: keys are the values among the 8(take away coverage of 
    bvk-vk3s), that are in [0..7], using sh-positions of the 3 top-bits.
    each tnode.vkm will have their vk12s all with the original bit-positions.
## 2021-03-31->0.184
- a difficult fix in vklause.partial_hit_residue
- still issue(seems) in 54.0-('57.3','60.6'): C0202 {3:0} should hit hsat
  and this shold set vkm.valid=False?
## 2021-03-31->0.183
- added some debugging print-out tools
- vk12m.info is now a list, no more dict, for better collecting infos
- vkm.bestchoice: get rid of bitsum comparison, use bits-compare, if
  len(touched) is the same.
## 2021-03-30->0.182
- fix the issue found for config1.json, where the tree is so shalow that the
  final occurs at level-1 (parent is top-level). Now config1.json get its sat.
- written doc0.txt
## 2021-03-29->0.181
- config1.json generated 0 sat?
- found issue: on pathmgr:35, should process finalize == True case! TBD
## 2021-03-29->0.180
- node12.collect_sat implemented.
- snode: done == final: self.tx_vkm.vkdic is empty.
- vk12m.debug controls print
- run for cfg12-55.json takes 0.018 sec
## 2021-03-29->0.179
- node12.done, replacing .valid, get rid of add_filtered_vkdic/remove_me
- node12.collect_sat using pathname TBD: not done yet
- pathmgr.dic key now is a tuple of tnode names: higher nov behinde
- vk12m.clone refactored: more efficient
## 2021-03-28->0.178
- refactored pathmgr.extend_vkm
## 2021-03-28->0.177
- minor optimization in tnode and vk12m.
## 2021-03-28->0.176
- fix in vk12m, solver11
## 2021-03-28->0.175
- fix a bug in vkmgr/morph(line 86): when building sub_vk12dic, use vk.clone()
  in staed of vk. For when constructing tnode, the vk may drop its bit. And this
  should not change the vk12 saved in snode.vk12dic.
## 2021-03-27->0.174
- use vk12mgr in tnode, get rid of prev methods in tnode(proc_vk1s, proc_vk2s,
  check_state, remove_kn and sort12, set-bmap)
- get rid of endnodemanager, candinode
- get rid of tnode.state, use tnode.vkm.valid
## 2021-03-26->0.173
- minor change in node12
- pathmgr: the value in .dic is no more vkdic, but a vk12mgr
- new rule in vkm.add-vk: (a + ^b)xb == axb, removing ^b from (a + ^b)
  This makes 9.2 + 12.0 be terminated right-away, before doing any 
  addition of 6.* + 9.2 + 12.0.
  This is now built in vk12mgr.add_vk (info in cfg12-55-analysis.txt)
## 2021-03-25->0.172
- progress on node12.
- pathmgr.extend_vkd now returns vk12m, no more vkd
## 2021-03-25->0.171
- node12.name -> .val, + other changes.
- PathManager constructor has a finalize optional param, if true,
  will create a node12 and solve it -> <class-var>.sats
- minor change in vk12mgr
- document analysis in docs/cfg12-55-analysis.txt
## 2021-03-24->0.170
- minor fix in  pathmgr. Clean up satnode.
- pathmgr works. May be better to render vkdic with node12, before save the path
  For some paths can be removed on this stage, early-rejection?
## 2021-03-24->0.169
- pathmgr: extend_vkd: need to also add vks from self.tnode.vkdic!
- some fixes in satnode
## 2021-03-24->0.168
- pathmgr.dic key is a chain of(concadinated)tn.val joined by '-'
- progress on pathmgr/chdic management in satnode. restrict_chs will be 
  obsolete after testing/verifying
## 2021-03-24->0.167
- progress in pathmgr.
## 2021-03-23->0.166
- SatNode now holds a class variable .maxnov. And a method: is_top()
- new class PathManager, an inst of it attached to each tnode, if its
  holder snode is not top-level.
- TBD: impl. and test
## 2021-03-22->0.165
- solver11. Based on solver10/## 2021-03-22->0.164
## 2021-03-22->0.164
- back to using cfg12-55.json, for analysis/ code-design.
- intro of pathdic in tnode, this records a vk12dic for each parent.ch-val, if
  there is a path to to highst nov. This replaces the previous tnode.pvs
- satholder offers a bit-tx-map, that maps: for each target-bit in gien t-sh,
  from the local bit. the starting-bits is a sub-set of local bits. This maps
  higher nov's sh(bits) to lower-nov's sh(bits)
- removed satholder.get_segment_sats
- vklause.partial_hit_residue changed. 
  TBD: endnodemananger.py: 34, and node12.py: 65, where this was used.
- minor fix in vk12mgr.py:98
- tnode: find_path_vk12dic.
  removed tnode.compatible_with
- satnode: restrict_chs now trims all ch-tnode with 0 pthdic, and parent.ch with
  0 time being refered from lower-tnode
  TBD: need to impl. 6.* to 9.* to 12.*
## 2021-03-19->0.163
- analysis on cfg60-266.json: written docs/cfg6-266.info.txt
## 2021-03-19->0.162
- class-variable EndNodeManager.tdic moved to class variable TNode.repo
## 2021-03-19->0.161
- solving cfg12-55.json, finding all 9 sats, using 0.035secs
- TBD: cfg60-266.json, stuck at snode18.
## 2021-03-19->0.160
- refactored endnodemanager, vk12mgr. update comment in vklause
- coding in node12
- getting right sats from 12.4-9.6-6.0(c,d,e,f,g), 12.4-9.2-6.1(h,i)...
## 2021-03-18->0.159
- vk12mgr.pick_bvk: when there is no vk1, pick vk2 -> max bit-sum
- node12:check_done
## 2021-03-18->0.158
- progress in endnodemanager, vk12mgr and node12
## 2021-03-18->0.157
- progress. vk12mgr now doesnt hold its hosting node12 inst. 
- code vk12mgr.morph, node12
## 2021-03-17->0.156
- progress
## 2021-03-17->0.155
- node12 replaing endnode, endnode-manager replacing satmgr.
- tnode.t_sh -> .sh
- snode.name (like sn12) removed, use .nov for name.
- coding endnodemanager, node12
## 2021-03-16->0.154
- refactored vk12mgr, satmgr, endnode, vkmgr
- node12
## 2021-03-16->0.153
- progress: made vk12mgr for n6.0 + n9.2 + n12.6 -> vk12mgr.valid == False
## 2021-03-15->0.152
- vklause has a new drop_bit method
- code vk12mgr. progress on endnode
## 2021-03-15->0.151
- vk12mgr from solver9
## 2021-03-15->0.159
- solved issue found in 0.158: merge hsas before do tn.check_sat
  cfg12-55.json: candis number from 43 reduced to 24 (delta:19)
- get rid of smgr.vdic
- t
node.check_sat has one more(optional) paramter:reverse_sh=def:False
## 2021-03-15->0.158
- progress in endnode and vklause/filter-hit
- TBD: candis[0]: [tn12.0, tn9.2, tn6.0] should not qualify for a candi:
  tn6.0-hsat + tn9.2-hsat has {9:0, 11:0}, this should hit tn12.0's C031.
  The error in candinode/find_candi: combination of all hsats should be
  tested (6.0 + 9.2 -> by 12.0 here), not the single ones.
## 2021-03-15->0.157
- progress on endnode/vklause
## 2021-03-15->0.156
- fix a bug introduced in 0.155
## 2021-03-14->0.155
- fix in vklause/hit for value is a sat-dic; fix in clone_tail
- progress in satmgr and endnode
## 2021-03-14->0.154
- satmgr.build_candis now can collect all paths
- bugged candinode it works now.
- TBD: I may do path ->sats converting in SatManager.
## 2021-03-14->0.153
- make use of SatManager.tdic's saved all tnodes. sat_array now holds only the 
  names of tnode.name. And tnode.check_sat will use that, and each candi-node 
  will save the check-results in a .vdic, so that previous check-result can be
  used.
## 2021-03-13->0.152
- SatManager has a new class-variable: tdic, holding every tnode under its name
- add pvs, hsat to tnode, where pvs is added/assigned not in contructor,
  but later when set-restrict 
- coding condinode/satmgr. Still on-going.
## 2021-03-13->0.151
- progressing on satmgr
## 2021-03-12->0.150
- minor fixes.
## 2021-03-12->0.149
- candinode to be used in satmgr 
- satmgr: coding: constructor.build_candis, resolve, 
- tnode now holds the hosting satnode as .holder
## 2021-03-12->0.148
- fix regression test found bugs. 
- remove chmanager.py
## 2021-03-12->0.147
- get rid of childmanager. put chdir directly under satnode
- endnode for the very last node where there is no vk3 left
- vklause has a new method: clone_tail, for endnode logic
- designing way for manage candis/sats...
## 2021-03-11->0.146
- git check-in, minor changes, but win10 has issue? be safe
## 2021-03-11->0.145
- fix in vkmgr/bestchoice: max_bitsum -> best_bitsum.
- tnode: when made, check its integrity: state=-1 when conflict makes it
  impossible to stand: this tnode will not be assigned to ch[val].
## 2021-03-11->0.144
- fixes in restrict and tnode
## 2021-03-10->0.143
- restrict.py, tnode.py
## 2021-03-09->0.142
- when reaching the last satnode, when vk3dic is empty, in case of cfg6-266.json
  the nov is 27, to do an exhaustive looping thru of 2**27, is exponential / bad 
  I did, consuming last 2 days (for test case of cfg12-55), how to do that in
  getting all possible sats in the satnode(nov3), and I am trying now to do this
  not with exhaustive going thru all 2**3(2**27).
## 2021-03-05->0.141
- start working on cfg60-266.json: for some reason, it hangs.
- childmanager holds a vk12dic, all chdic-vk12s are refs to this dic.
## 2021-03-05->0.140
- redesigned satholder/iterator going thru all :2's 
- completed satmgr: it works for cfg12-55.json, finding all 9 sats
  correctly (0.018388 secs)
## 2021-03-05->0.139
- yesterday, I did a all manual crawl through, finding all 9 sats correctly,
  using the trees.
- did some refactoring today
## 2021-03-04->0.138
- progress in SatMgr
- fix in crownmgr
## 2021-03-03->0.137
- crownmanager.chdic now has 
  ['vk12dic']={<vkdic>}
  ['parent-ch-keys'] = [<int-keys of parent crwnmgr.chdic>]
  ['hsat'] = {sat of head}
- satmgr in progress
## 2021-03-03->0.136
- basics/verify_sat now accpt sh, to reverse sat with sh.
- satholder.reverse_sdic
- crownmanager.raw_crown_dic moved to __init__, changed name: chdic
- crownmgr.set_restrict impl; .parent ref to higher crownmgr.
## 2021-03-02->0.135
- clean up a bit
## 2021-03-02->0.134
- branch off solver10 from solver9.
- get rid of node12/vk12mgr
## 2021-03-02->0.133
- vkmgr.bestchoice: when tsvk/tcvk are the same length, choose the one with bits
  sitting higher positions. This make the choice reproduceable.
## 2021-02-27->0.132
- SatMgr
## 2021-02-26->0.131
- minor fixes.
## 2021-02-25->0.130
- minor fixes.
## 2021-02-25->0.129
- minor fixes.
## 2021-02-24->0.128
- small fixes
## 2021-02-24->0.127
- new design: leave crowns un-resolved, first do satnode.next_>next,... untill 
  the satnodehas 0 vk, of nov==3. Then use the sat resulting from here(it may
  have :2 in it), as satfilter to resolve this satnode's crowns. The result of 
  that, will be used as satfilter for .parent satnode.
- TBD: code/test
## 2021-02-18->0.126
- new: basics/vkdic_sat_test, /vkdic_remove
-satnode: when psat returns a dict{1:{}, 2:[]}
## 2021-02-18->0.125
- test with cfg12-55.json, it has 9 sats(solver4 used 0.053735971450805664):
   [915, 2362, 2325, 2320, 2321, 2322, 2323, 785, 787]
   a.(915):   001110010011
   b.(2362):  100100111010
   c.(2325):  100100010101
   d.(2320):  100100010000
   e.(2321):  100100010001
   f.(2322):  100100010010
   g.(2323):  100100010011
   h.(785):   001100010001
   i.(787):   001100010011
ray@thinkpad-x1:~/lab/solver9$ python solver9.py cfg12-55.json
there are 9 sats:
1: { 11: 0, 10: 0, 9: 1, 8: 1, 7: 0, 6: 0, 5: 0, 4: 1, 3: 0, 2: 0, 1: 0, 0: 1 }, verified: True
2: { 11: 1, 10: 0, 9: 0, 8: 1, 7: 0, 6: 0, 5: 0, 4: 1, 3: 0, 2: 0, 1: 0, 0: 0 }, verified: True
3: { 11: 1, 10: 0, 9: 0, 8: 1, 7: 0, 6: 0, 5: 0, 4: 1, 3: 0, 2: 0, 1: 0, 0: 1 }, verified: True
4: { 11: 1, 10: 0, 9: 0, 8: 1, 7: 0, 6: 0, 5: 0, 4: 1, 3: 0, 2: 1, 1: 0, 0: 1 }, verified: True
5: { 11: 0, 10: 0, 9: 1, 8: 1, 7: 0, 6: 0, 5: 0, 4: 1, 3: 0, 2: 0, 1: 1, 0: 1 }, verified: True
6: { 11: 0, 10: 0, 9: 1, 8: 1, 7: 1, 6: 0, 5: 0, 4: 1, 3: 0, 2: 0, 1: 1, 0: 1 }, verified: True
7: { 11: 1, 10: 0, 9: 0, 8: 1, 7: 0, 6: 0, 5: 0, 4: 1, 3: 0, 2: 0, 1: 1, 0: 0 }, verified: True
8: { 11: 1, 10: 0, 9: 0, 8: 1, 7: 0, 6: 0, 5: 0, 4: 1, 3: 0, 2: 0, 1: 1, 0: 1 }, verified: True
9: { 11: 1, 10: 0, 9: 0, 8: 1, 7: 0, 6: 0, 5: 1, 4: 1, 3: 1, 2: 0, 1: 1, 0: 0 }, verified: True
Time used: 0.008216619491577148
1->h, 2->d, 3->e, 4->c, 5->i, 6->a, 7->f, 8->g, 9->b. 
All right.
- testing cfg60-266.json, run into issue with Exception: 
  TBD: there are 32 entries with :2, 
  in basics.py:75. Need to design a way to handle this.
  solver4.py found 8 sats using 26.8 secs.

## 2021-02-17->0.124
- minor fix in crown.py/satnode.py so config1.json with nov==8 comes thru.
## 2021-02-15->0.123
- now all 7 sats from cfg12-45.json are found right, with built in verification
- FINAL['limit'] set to be 10
- basics/verify_sat for verifying sat in solver9
- intro of satnode.tail_varray: verify tail-satnode, where it is used for
  sh-shifting vk.bits so that they can be compared with satfilter 
- satnode.verify_tail_sat
- refactore solver9
- TBD: when there are more than 3 sat entries with :2 - should I do recursion
  with satnode(nov - 3)? This issue will apear when the number of variables is
  high: now I am testing with cfg12-45, with 12 vars. 
  I will be analyzing and redesigning when doing bigger var-numbers, later.
## 2021-02-15->0.122
- polishing and completion in basics, satnode, solver9.
  cfg12-45.json: 
ray@thinkpad-x1:~/lab/solver9$ python solver9.py
there are 7 sats:
1: { 11: 1, 10: 0, 9: 1, 8: 1, 7: 0, 6: 0, 5: 1, 4: 1, 3: 0, 2: 0, 1: 0, 0: 1 }
2: { 11: 1, 10: 0, 9: 1, 8: 1, 7: 0, 6: 0, 5: 1, 4: 1, 3: 1, 2: 0, 1: 0, 0: 1 }
3: { 11: 1, 10: 0, 9: 1, 8: 1, 7: 0, 6: 1, 5: 1, 4: 1, 3: 0, 2: 0, 1: 0, 0: 1 }
4: { 11: 1, 10: 0, 9: 1, 8: 1, 7: 0, 6: 1, 5: 1, 4: 1, 3: 1, 2: 0, 1: 0, 0: 1 }
5: { 11: 1, 10: 0, 9: 1, 8: 1, 7: 0, 6: 0, 5: 1, 4: 1, 3: 0, 2: 1, 1: 0, 0: 0 }
6: { 11: 1, 10: 0, 9: 1, 8: 1, 7: 0, 6: 0, 5: 1, 4: 1, 3: 0, 2: 1, 1: 0, 0: 1 }
7: { 11: 0, 10: 1, 9: 1, 8: 1, 7: 1, 6: 1, 5: 1, 4: 1, 3: 0, 2: 0, 1: 0, 0: 1 }
  Time used: 0.008653402328491211
7:b 

## 2021-02-15->0.121
- basics/split_satfilter: if sdic has x:2 in it, 1 or n times, split sdic into
  1 or n: exhaust all (n<4) 2 ** n combinations. return a list of sdics.
- get rid of basics/merge_sats and merge_satdics
- satnode.verify_sat: when satfilter has no :2 in it, verify it with vk3 in .vkm
- satnode handles multi-sats collection in FINAL.
- vklause.hit now accept sdic as input.
## 2021-02-13->0.120
- see log.txt entry : ## 2021-02-13: analysis on a new satnode design, where
  it can handle psats with diff number of ':2'.
## 2021-02-12->0.119
- extend basics/deb_01 to cover 12.6.1 and 12.6.2
- TxEngine.trans_varray has again the 
  assert(self.start_vklause.nov == len(varray)) this check is right to be there.
- satnode.crown-mananger.sh and satnode.next(satnode).sh should be 2 insights
  now use sh.clone to make sure of that.
- TBD: from the 7 solutions(a,b,c,d,e,f,g), 
  12.4.2 should cover d, but it didn't 
  12.4.3 should cover e, but it didn't 
  12.4.5 should cover f, but it didn't 
  12.4.6 should cover g, but it didn't 
  12.6.1 should cover a and b, but it didn't.
  12.6.2 should cover c, but it didn't. 
## 2021-02-12->0.118
- move crownmanager/_oppo to basic/oppo_binary
- TxEngine constructor: use vk.nov, in stead of extra nov as input param.
- remove TransKlauseEngine.py/trans_varray/assert(self.nov == len(varray))
  not sure why this has cause issue.
- made sure crown-mamager/add_crown: when creating a new crown, use 
  self.sh.clone, not self.sh to feed Crown instance.
## 2021-02-11->0.117
- fix in crown
## 2021-02-10->0.116
- fix in crownmanager/._vk2_sdic
## 2021-02-10->0.115
- fix in crown, new debug function in basics; optimize in 
  crownmanager/._vk2_sdic
## 2021-02-10->0.114
- fix in crown: when vk12m is a list, make the right csats: [psats,[]]
- refactor basics/filter_sdic, node12, satnode
- fix in crownmanager/_vk2_sdic
## 2021-02-09->0.113
- optimized vk12mgr a bit.
## 2021-02-08->0.112
- progress on node12/nov3_sats -> nov321_sats; satnode.py and solver9
## 2021-02-08->0.111
- refactored crown.csats: a list of csats - each path from crown to leave node12
  there will be a sat-path resulting to one or multiple sat(s).
  each csat is a list of 2 elements:
    [<sdic along the path, without last node12's sats>, [last sats]]
  the last node12 may have multiple sats. So this csat may have multiple sats:
  [0].update([1][i]). When delivering a csat, crown will maintain a .sub_curosr
  only when it overflows (bigger than len(last sats)), will csat_cursor increase
  and, when all csats of a crown are exhausted, will crownmananger.crown_index
  gets increased. When all crowns are exhausted, crownmanager.state set to 1
  This is a prep for collecting all possible sats.
- basic/FINAL is the final sats collector, it can also limit how many sats 
  should be collected,
- TBD: finish the multiple-sat collection, and testings.
## 2021-02-06->0.110
- progress on crown and node12.
## 2021-02-06->0.109
- crown and node12 have satpath - a list of sdics, from crown all the way 
  to this node12. The leave-node12 will add an array of sdics. 
  The leave-node12 will be in crown csats list. When crown delivers its 
  solution sat, it will loop thru all ele in its csats: each has array of
  sdics, each of which will combine with the whole satpath to form a complete
  sat-dic.
## 2021-02-05->0.108
- refactoring on basics, crown, crownmanager, node12, satholder, satnoce.
- TBD: figure out a way to collect sats: bottom(leave node12) up ...
## 2021-02-03->0.107
- successfully found 1 sat(f) with 0.018secs. solver4 found all 7 for 0.046 secs
- TBD: find all sats.
## 2021-02-03->0.106
- fix in crownmanager/_vk2_sdic(vk)
## 2021-02-03->0.105
- fix in node12: when chdic[<val>] == None, set node12 with sh.full_sats
## 2021-02-03->0.104
- crown-mananger.next_psat no more set solution_cursor = 0. Done in .init()
- satnode adds ._clone_chdic, making crown_dic a clone of self.raw_crown_dic
- tx_vkm now attached to self(satnode instance)
## 2021-02-02->0.103
- fix a bug in satnode.
- TDB: 1. crownmgr.next_psat always reset solution_cursor; 2 satnode has issue.
## 2021-02-01->0.102
- using satfilter in crown.solve
- TBD: more testing
## 2021-02-01->0.101
- refactored node12 and crown.
- TBD: satfilter needs to put into crnmgr.next_psat.
## 2021-01-30->0.100
- progress.
## 2021-01-29->0.99
- crown.initial_nodes: when no vk exists (len(vkdic)==0), vkm.terminated = True
  and in vkm.morph, if terminated==True and no vk, chdic[val] = None.
  This chdic[val]==None will set crown.child_satdic[val] = sh.full_sats()
- child_satdic will be keyed by val, no more by node.vname. So is the case also
  in node12.child_satdic.
- TBD: testing
## 2021-01-29->0.98
- minor optimization in crownmanager: init no more called in constructor.
## 2021-01-29->0.97
- CrownManager: separates a method .init(), for reset crowns list 
  This should be called every time satnode.spawn is called. Because it has a 
  different satfilterfilter every time it is called. This satfilter comes from 
  one of the node12's that are made by different satnode.parent children.
- satnode.spawn now has the call self.crnmgr.init() in it.
## 2021-01-28->0.96
- cfg12-45.json has 7 sats:
  [2017, 2033, 3953, 2865, 2873, 2929, 2937]: [a,b,c,d,e,f,g]
2017:011111100001 {11:0, 10:1, 9:1, 8:1, 7:1, 6:1, 5:1, 4:0, 3:0, 2:0, 1:0, 0:1}
2033:011111110001 {11:0, 10:1, 9:1, 8:1, 7:1, 6:1, 5:1, 4:1, 3:0, 2:0, 1:0, 0:1}
3953:111101110001 {11:1, 10:1, 9:1, 8:1, 7:0, 6:1, 5:1, 4:1, 3:0, 2:0, 1:0, 0:1}
2865:101100110001 {11:1, 10:0, 9:1, 8:1, 7:0, 6:0, 5:1, 4:1, 3:0, 2:0, 1:0, 0:1}
2873:101100111001 {11:1, 10:0, 9:1, 8:1, 7:0, 6:0, 5:1, 4:1, 3:1, 2:0, 1:0, 0:1}
2929:101101110001 {11:1, 10:0, 9:1, 8:1, 7:0, 6:1, 5:1, 4:1, 3:0, 2:0, 1:0, 0:1}
2937:101101111001 {11:1, 10:0, 9:1, 8:1, 7:0, 6:1, 5:1, 4:1, 3:1, 2:0, 1:0, 0:1}

- cfg60-266.json has 8 sats: 
  solver4 uses 20+secs, solver8 uses 3 secs for 1 sat (a)
  solver8 uses 3+ secs finding one sat 
 1034639552019849453, 1034639552086958317, 1034639552556720365,
 1034639552623829229, 1043646751274590445, 1043646751341699309,
 1043646751811461357, 1043646751878570221]:
 0: 1110010110 1111000111 0011000011 0110001011 0110011000 0011101101
 1: 1110010110 1111000111 0011000011 0111001011 0110011000 0011101101
 2: 1110010110 1111000111 0011000011 1110001011 0110011000 0011101101
 3: 1110010110 1111000111 0011000011 1111001011 0110011000 0011101101
 4: 1110011110 1111000111 0011000011 0110001011 0110011000 0011101101
 5: 1110011110 1111000111 0011000011 0111001011 0110011000 0011101101
 6: 1110011110 1111000111 0011000011 1110001011 0110011000 0011101101
 7: 1110011110 1111000111 0011000011 1111001011 0110011000 0011101101

## 2021-01-28->0.95
- start testing with cfg12-45.json
- optimization in node12, and crownmanager(iterative replace recursion)
- fix in crown/resolve
## 2021-01-27->0.94
- success with config1.json
## 2021-01-26->0.93
- basics/sdic_fail(d0, d1) also set d1's value from 2 to 0|1 if d0 requires that
- TBD: how to get the final sats, with crown/psats. Need more analysis.
## 2021-01-26->0.92
- progress: basics/sdic_fail: used in satnode/filter_children, and 
  crownmanager.add_crown now also uses satfilter to not add crown if csats fails
  to be checked against satfilter. This reduces search space.
## 2021-01-25->0.91
- progress: don't create self.next ( an inst of SatNode) in constructor. But
  when needed.
## 2021-01-25->0.90
- re-designed/impl. of satnote, interaction between it and crownmanager/crown.
- test not yet done.
## 2021-01-24->0.89
- satnode.filter_children - how to loop  TBD
## 2021-01-23->0.88
- progress on cown, crownmanager and satnode.
## 2021-01-23->0.87
- fixes in crownmanager._vk1_sdic/._vk2_sdic, and in crown.
## 2021-01-22->0.86
- re-code vk12m.morph. bvk_cvs no more needed.
## 2021-01-22->0.85
- impl vk12m.morph the same way as in vkm.morph. TBD: test
## 2021-01-21->0.84
- refactored vkmgr/morph, and vk12m: now use vkdic, and kn1s/kn2s
- TBD: vk12m.morph
## 2021-01-20->0.83
- simplify what last checked in.
## 2021-01-20->0.82
- recode vkmgr.morph, and crownmanager/satnode.
## 2021-01-20->0.81
- optimized vkmgr.bestchoice: take away all tsvk kns from candidates - Because
  a kn can not be in >1 best-keys. This reduce the loop-count.
## 2021-01-19->0.80
- possible bug in vkmgr.py/morph: I should loop thru all 2**3 == 8 vals?
  TBD: analysis
- coding in crown and crownmanager for covering when only 1 vk left.
## 2021-01-18->0.79
- fix in satnode cdic[1] > cdic.get(1,{}), cdic[2] > cdic.get(2, {})
- progress on handling the case of cown top-level node with only 1 vk
## 2021-01-18->0.78
- refactored/fixed/optimized satnode and vkmananger. Still backwards compatible.
## 2021-01-17->0.77
- change crown.csats to be list of tuple: (sat-dic, leef-node12-name). Because
  a crown may have multiple sat-dics.
## 2021-01-17->0.76
- tested with config1.json: crown/node12 start working, and deliver psats with 
  {7:1, 6:2, 5:1, 4:0, 3:1, 2:0, 1:1, 0:0}, where 6:2 means a wild-card for v6.
## 2021-01-15->0.75
- move merge_sats from node12 to basics.
- progress on managing sats-branching, from crown to bottom-level node12.
  Need more testing
## 2021-01-14->0.74
- fixing crown, vk12m.
## 2021-01-13->0.73
- progressing.
## 2021-01-12->0.72
- new design / impl.: crown/crown-manager, interactions with satnode. 
  Not yet finished.
## 2021-01-11->0.71
- sat2 partial sats management in node12
- TBD: interaction between node12 and satnode.
## 2021-01-11->0.70
- progress on vk12mgr and node12, on collecting sats. Some refactoring on both.
## 2021-01-10->0.69
- fixes in vk12mgr and node12.
## 2021-01-08->0.68
- tested vk2 as bvk (multiple), and if bvk_cvs counts 4 (2**2 ==4)
  then no space left -> self.terminated = True
- vk12m.bvk_cvs is a set, no more list.
## 2021-01-08->0.67
- tested vk12m.best_vk2, with manually deleted vk1dic in config1,json
  setting.
- refactored some.
## 2021-01-08->0.66
- code for vk12m: in case no vk1 exists, pick the best vk2. Always set a list
  self.bvk_cvs, either from vk1 bvk or vk2 bvk. Now in morph, test if a value
  is in self.bvk_cvs, for exclusion.
- refactored 
## 2021-01-07->0.65
- enhanced satholder with get_psats dic for tracing {var>:<val>,..}
- refactored/optimized basics/node12/satnode
- TBD: issue: vk12m - if no vk1, when picking bvk, there can be multiple
  vk2 sitting on the same 2 bits, in that case exccl-cvs?
  And, how pick the best vk2?
## 2021-01-06->0.64
- minor fix. The approach introed by 0.63 works!
## 2021-01-06->0.63
- believe found the bug/fixed: when doing vk12m.clone(), bvk not set.
  this causes isse when calling topbits_coverages(vkm.bvk, topbits)
  Solution: vk12m.txed_clone or vk12m.clone both will NOT set bvk.
  But vk12m now has a method .bvk_topvalue. Node12.spaw(): before doing
  tx, get cv = self.vk12m.bvk_topvalue() and use this cv in vk12m.morph
  This also optimized away topbits_coverages in node12 and vk12m.
- TBD: test it
## 2021-01-06->0.62
- optimized a bit for VK12Manager constructor: choices for call/not-call
  of make_bdic and normalize.
- still need to find/fix the bug in 0.61
## 2021-01-05->0.61
- effort to pick default vk1 as bvk with the 1 bit sit on highst pos.
  This can  optimize. But this has brought in a bug. Need to find it.
  TBD.
## 2021-01-05->0.60
- give node12 inst a name. children is a list now (was dict)
- pick highst bit vk1 as default bvk in vk12m
- tried node12.spawn (9-7/8-1/7-1/6-1/5-1/4-1/3-1) to the end: 
  sofar so good
## 2021-01-04->0.59
- refactored/fixed vk12mgr, and node12
- made satnode's loop thru children with sorted val-keys. When loop with
  for k, v in dict.items(), it is really not deterministic about the calling
  sequence. I need that in debugging.
- tested cfg12-45's children(1,2,3,4,5,6,7)'s spawn. With the reduction in
  child-5's C0016/C0045 removed by nov==8/vk1:C0044
  child-6's C0013/C0002 removed by nov==8/vk1: C0014/C0009
  So far node12 works fine with vk12mgr.
  TBD: node12.spawn all the way till one child finds sats?
## 2021-01-04->0.58
- progress on vk12m / node12
## 2021-01-04->0.57
- coded vk12mgr/morph, node12/spawn
## 2021-01-03->0.56
- progress on vk12mgr.py and node12.py
## 2021-01-03->0.55
- Node12 will take care of vk12dic, for every satnode's child.
- new class VK12Manager / vk12m.py
## 2021-01-02->0.54
- When making crowns in vkm.morph, now consider bvk cover value (blokc it)
- progress in crown.py
## 2020-12-31->0.53a
- cfg12-45.json has 7 sats: 
  [2355, 2363, 2419, 2427, 3299, 3315, 3443]. in 9-12 space (max 512):
  [2355, 2363, 2419, 2427] are in 4-th subspace: [307, 315, 371, 379]
  [3299, 3315, 3443] are in 6-th subspace: [227, 243, 371]

- analized cfg12-45 split behavior. After txed on C0006{10:0,8:0,1:0} and 
  C0017 {10:1,8:1,1:1}->[11,10,9], there are 12 vk3 left untouched,31 touched.
  cfg9-12.json (for 12 left in vkdic): 
  123 x sats: [ # in the 512 value-search-space #
    0  1  2  3  4  6  8  9  10 11 20 32 33 34 35 36 38 40 41 42 
    43 48 49 50 51 52 56 57 58 59 64 65 66 67 68 70 72 73 74 75 76 78 84 
    96 97 98  99  100 102 104 105 106 107 108 110 112 113 114 115 116 120 
    121 122 123 124 129 131 136 137 161 163 168 169 177 179 184 185 193 
    195 200 201 204 225 227 232 233 236 241 243 248 249 252 304 305 
    306 307 308 309 312 313 314 315 340 368 369 370 371 372 376 377 
    378 379 380 433 435 437 440 441 497 499 504 505 508 
  ]
  from the 8 children, 0 and 7 are covered by base C0006 and C0017.
  all 8 children:
  0: cfg12-45-0-9-17.json (17=vk1s + vk2s): no sat
     cfg12-45-0-9-29-vk123.json (29: all vks): no sats 

  1: cfg12-45-1-9-18.json (18=vk1s + vk2s): no sat
     cfg12-45-1-9-30-vk123.json (30: all vks): no sats 

  2: cfg12-45-2-9-13.json (13=vk1s + vk2s): 1 sat: [270] not in cfg9-12's sats
     cfg12-45-2-9-25-vk123.json (25: all vks): no sat

  3: cfg12-45-3-9-13.json (13=vk1s + vk2s): no sat
     cfg12-45-3-9-25-vk123.json (25: all vks): no sats 

  4: cfg12-45-4-9-13.json (13=vk1s + vk2s): 9 sats:
        [283,307,310,311,315,347,371,375,379]:[307,315,371,379] in 9-12 sats
     cfg12-45-4-9-25-vk123.json (25: all vks): [307,315,371,379]

  5: cfg12-45-5-9-14.json (14=vk1s + vk2s): 2 sats:[261,277] all not in 123 sats
     cfg12-45-5-9-26-vk123.json (26: all vks): no sats 

  6: cfg12-45-6-9-10.json (10=vk1s + vk2s): 8 sat:
       [227,231,243,247,355,359,371,375], [227, 243, 371] in 123 sats
     cfg12-45-6-9-22-vk123.json (22: all vks): 3 sats:[277, 243, 371]

  7: cfg12-45-7-9-17.json (17=vk1s + vk2s): 2 sats: [227, 243] both in 123 sats
     cfg12-45-7-9-20.json (29: all vks): 2 sats: [227, 243]
  
## 2020-12-31->0.52
- crown now has vk1dic/vk2dic, saved under child-dic[val]. The sum vk12dic is 
  saved on parent/self .vk12dic
- looking into cfg12-45 case, for design analysis: txed with C0006/C0017 as base
  all sollution *.tx files saved under docs
## 2020-12-30->0.51
- vkmgr.py: new class VKManager.
- satnode.py: new class satnode
- get rid of bitdic, branch, relationmanager and workbudder
## 2020-12-28->0.50
- debug rm
- realized, that untouched should be seperated from touched:
  touched is child-specific, but untouched should be shared among all
  children: solve the next level with untouched(without touched). the solution
  can be combined with every child of the parent-br.
- although the br is based on first 3-bits (bestkey), but the other 3-bits
  keys, are they needed?
## 2020-12-27->0.49
- coding rm.
## 2020-12-26->0.48
- progress
## 2020-12-25->0.47
- new class RelationManager.
## 2020-12-25->0.46
- brached from solver8 -> solver9
  Plan to try out enhancing bitdic: relations-manager
  inside bitdic, or outside? Holding vks-dic, vk2-dic and vk1-dic?
## 2020-12-25->0.45
- minor polish, before branching off to solver9
## 2020-12-24->0.45
- found bugs: 1. Tx: wrong generated odd number of txs? fixed: using set ops
- vklause.clone(drops) can return empty vk.dic, in that case, not adding to vkd.
- cfg100-450 now uses 113 secs. Much better now, but still room to optimise.
## 2020-12-23->0.44
- branch/spawn untouchset vks will not be txed: no need to clone for every
  child bitdic. Share them will save some run.
## 2020-12-22->0.43
- Tx: txs no more a list of tuples, but dict. get rid of trans_value 
  reverse_value stuff.
- use class variable Branch.LAYERS for holde the tree
- cfg100-450.json failed to have result - debugging
## 2020-12-22->0.42
- get rid of visualizr.py, TransKlauseEngine.test_me, vklause.value_overshadow 
  vklause.set_completion,.position_value, move set_value_and_mask from __init__
  tp vklause.hit.
- in BitDic, move add_vk to be a method - no more inside of add_klause
  All these reduced run ti
  m for cfg100-450.json from 168 secs to 164
  cProfile time from 260 to 231 secs (see docs/## 2020-12-21-042=100-450.info)
- Branch/spawn: check for outdics length==1 and have opposite 0/1: 
  this branch-child is not to exist
- BitDic get_choice now returns changed...
## 2020-12-21->0.41
- get rid of nbits in vklause. This reduced cProfile run time for 
  cfg100-450.json from 542secs to 277 sec.
  see (see docs/## 2020-12-21-041=100-450.info)
## 2020-12-21->0.40
- cfg100-450 with solver4 was 438(533 secs cProfile) secs returning all sats. 
  Now solver8 return only 1, but use 488(542secs cProfile) secs
  (see docs/## 2020-12-21-040=100-450.info)
  I am disappointed. But using python -m cProfile gave me some insights, for
  optimization.
## 2020-12-21->0.39
- verification not run on normal process. *.sat file now have more info.
  python solver8.py *.sat will verify the sat in sat file
## 2020-12-20->0.38
- choice returned by BitDic.get_choice now has 3 in the tuple:
  kn, tsvk, tcvk, so that the kn will not be popped from tsvk
- branch.nov3 now uses set ops to simpify. It works.
## 2020-12-20->0.37
- refactored bitdic having new get_choice and best_choice. remove transfer
- get rid of makechoice.py
- moving topbits_coverages to basics, get rid of drop_bits
## 2020-12-19->0.36
- best choice will be made among the shortest vks. At beginning it is 3-bits,
  but down the tree 1,2 are preferred.
- before making choice among vk1s, check if they cover totality
  totality means: among the 1 bit vk, there exist two sitting on the same bit,
  with opposite values(0 and 1)
- if branch has totality, of spawned no children, it is renamed 'finished',
  and it is removed from parent's children-dic
## 2020-12-19->0.35
- based on solver7/0.34
## 2020-12-18->0.34
- Sat.nov class var holding nov. In Sat.verify looping thru vks, make
  sure vk.bits[0] < Sat.nove - safty guard.
## 2020-12-18->0.33
- VKlause.hit now can test if vk is hit by a sat( lst of tuples)
- python solver7.py *.sat will verify *.sat file
## 2020-12-18->0.32
- new class Sat for verifying and saving into .sat file
- VKlause.hit test now also accept v as a list of pairs: (<bit>,<bool-value>)
- WorkBuffer.build_sats: use the end-node, trace all the way back to root
  and collecting segment-sats to build a complete sat-array.
- it works on config1.json, verified, and outputted in verify/config1.sat
## 2020-12-17->0.31
- put satholder in use, workbuffer/build_sats make the final sats
  still bug: in [(3, 1), (5, 1), (6, 1), (0, 1), (7, 1), (1, 0), (2, 0), (4, 0)]
  last 2 bits should be (0,0),(1,1), not (0,1),(1,0)!
  But still big progress.
- TBD: make solver7/verify_sats
## 2020-12-16->0.30
- introducing SatHolder mechanism. Done incomplete impls: TBD
## 2020-12-15->0.29
- if nov becomes 3, check for sats
- in makechoice/best_vk1: handle when no g1-vk exists.
- on level-0 branch, parent is original bitdic. lower brs will
  have branch as parent.
## 2020-12-15->0.28
- move basic stuff into basics, make_vkdic to bitdic
- add branch/nov3() for testing nov==3 coverage,... TBD
## 2020-12-14->0.27
- run till" r->(r1, r5, r7) ->{r11, r51} ->{r110 } ->{r1101}
  r1101: nov==2: C032:{0:0}, C004: {1:0}
  @ branch.py:65/chdic = self.prepare() having issue @makechoice.py:243
  max argument empty. I am near to my near goal!
## 2020-12-14->0.26
- vklause now has a method: .value_overshadow(vkx), testing if, in case 
  self.dic has the same number of, or less bits than vkx, if the value-range 
  of vkx is already covered by self. this is useful when testing vk1 or
  later vk2
## 2020-12-14->0.25
- bug fixes.
- TBD: r7 has issue. It should resolve.
## 2020-12-13->0.24
- refactored wb, bitdic, branch
## 2020-12-12->0.23
- debugging workbuffer
## 2020-12-11->0.22
- design the structure of method on high level
## 2020-12-10->0.21
- move drop as BitDic method to outside of BitDic: drop_bits
## 2020-12-10->0.20
- solve_vk1 in progress
## 2020-12-10->0.19
- choice-dic did not break 3-bit processing, and getting to vk1.
## 2020-12-09->0.18
- progress: best_vk1/2/3 all return a choice-dic, in stead of a list
## 2020-12-09->0.17
- progress on 1. makechoice for vk1, branch/spawnoff1,..
## 2020-12-08->0.16
- branch/pickon_vk1, and more stabs in branch
## 2020-12-08->0.15
- first stage(nov==8 -> nov==5) done
- vklause adds topbits(), changed mask to value.
## 2020-12-07->0.14
- cnt/cvrs is now a dict keyed by cover-v, value: set of kns
- branch spawnoff:  hitdic for values hit, and children, for further search
- manually made b0-1.txt, b0-5.txt b0-7.txt for analysis of child-search
## 2020-12-06->0.13
b0 split to 1,5,7 success
makechoice/topbits_coverages modified, verified
## 2020-12-06->0.12
makechoice/topbits_coverages
## 2020-12-05->0.11
progress
## 2020-12-05->0.10
progressing
## 2020-12-04->0.9
progress
## 2020-12-04->0.8
choice now has 
 [(<base-vkname>,..), (<cover-values), g2dic, [g1-list], [g0-list]]
cretarium: it has the 1. most cover-values, 2. most g2s
## 2020-12-03->0.7
progress: branch.py used in solver7, using bitdic and TxEngine.
## 2020-12-03->0.6
TxEngine, BitDic
## 2020-12-02->0.5
make_choice done
## 2020-12-01->0.4
start working: makechoice
## 2020-11-30->0.3
progress
## 2020-11-30->0.2
makechoice.py - started, not yet finished how to pick the best 3-bits vklause
## 2020-11-28->0.1
New approach: solver7, based on Tx. But this time split into 8 R0..R7
in stead of 2.