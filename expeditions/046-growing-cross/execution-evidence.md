# Actual execution evidence

Code checkpoint: [6d632a3e5392bde5fc4b005d4790e52747f8e47e](https://github.com/yo4e/PvsNP-Cartography/commit/6d632a3e5392bde5fc4b005d4790e52747f8e47e), tree 0bf1b51f162a912a32ac421665238f2223632ea8.

After publishing the code checkpoint and moving main with the expected parent, fetched main's ref, commit metadata, check.js and results.json at the immutable commit. Observed:

    main = 6d632a3e5392bde5fc4b005d4790e52747f8e47e
    check.js blob = efb4af189cee830cb29e24311e08be3ea573c00a
    results.json blob = 418e011e222a3dd239284b2044d67d4145b6cfb7
    exact replay equality = true
    local gate charge cases = 72
    direct odd parity counts = [16,64]
    fixed-layout counting control = 16 affine tables; 144 covered; 112 uncovered

The readback replay executed the retrieved source in the V8 tool runtime, replacing only the final console.log wrapper by return expedition046(), then compared JSON.stringify of the full returned object with JSON.stringify of the retrieved parsed results. Equality held. Initial and repaired versions also ran before their respective writes; an earlier immutable readback of 52618f1e reproduced the initial result exactly. This is an actual executable replay, not a claim of a GitHub Actions run or a second implementation/proof kernel. The script has explicit throwing checks. On a local Node runtime it is intended to run as: node check.js > actual.json, then compare actual.json to results.json. Node execution and CI are not claimed for this session.

The script uses packed BigInts for seed rows, a generated signed DAG and actual private-copy rewiring, and separate absolute-point scalar interpolation for the tested field assignments. Direct parity checks sum original rows rather than transformed values. All nonaffine row signatures, occupied tag identities and rank injections are tested; the padding completion is represented by an explicit formula, not expanded to the entire very large cube. It verifies the finite controls at a=3,4 only. Gate charging, exact NO minimum, asymptotic gate bound and the explicit family degree upper bound have separate written arguments. No new Lean acceptance or independent external review.

Earlier code commits: 52618f1ecf94b0e1681cdbe6f47419d6a86cda92 (initial generator and layout), 3f65f836ffb41f4aeb993b4d2c2bdc2182624a4e (separated constants and compact obstruction), f2b01f47fca3de198a6aee092ee4a982ed22adce (unequal-prefix layout and mapped failure replay). The final code adds inverse-sibling and literal-charge controls plus direct parity witnesses.
