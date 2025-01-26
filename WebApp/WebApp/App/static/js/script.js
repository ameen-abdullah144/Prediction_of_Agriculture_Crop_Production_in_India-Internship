document.addEventListener('DOMContentLoaded', function() {
    updateVarieties();

    const cropSelect = document.getElementById('crop');
    cropSelect.addEventListener('change', updateVarieties);

    // Adding ripple effect to the button
    const buttons = document.querySelectorAll('button');
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            let x = e.clientX - e.target.getBoundingClientRect().left;
            let y = e.clientY - e.target.getBoundingClientRect().top;

            let ripple = document.createElement('span');
            ripple.style.left = `${x}px`;
            ripple.style.top = `${y}px`;
            this.appendChild(ripple);

            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });

    // Form reset and repopulate dropdowns
    const form = document.querySelector('form');
    form.addEventListener('submit', function() {
        setTimeout(() => {
            form.reset();
            updateVarieties();
        }, 100);
    });
});

function updateVarieties() {
    const crop = document.getElementById('crop').value;
    const varieties = {
        "Paddy": ["Chinsurah Rice (IET 19140)", "(CNI 383-5-11)", "IGKVR-1 (IET 19569)", "IGKVR-2 (IET 19795)", 
                  "CR Dhan 401 (REETA)", "CR Dhan 601 (IET 18558)", "CR Dhan 501 (IET 19189)", "RC Maniphou 11 (IET 20193)"],
        "Wheat": ["MPO(JW) 1215 (MPO 1215)", "MACS 6222", "PDW 314", "DBW39", "VL Gehun 907 (VL 907)", "Pusa Suketi HS 507", 
                  "Pusa Prachi (HI 1563)", "WHD 943", "Netravati (NIAW 1415)"],
        "Barley": ["BH-902", "DWRB 73", "Pusa Losar (BH-380)"],
        "Maize": ["HSC1", "HQPM-4", "MCH 36 (Hybrid) (DKC 9099)", "DHM 119 (BH 4062)", "PMH 4 (JH 31153)", "PMH 5 (JH 3110)"],
        "Pearl Millet": ["Nandi-65 (MH-1549)", "Nandi-61 (MH-1548)", "86M64 (MSH 203) (Hybrid)", "MH 1540 (86M64) (Hybrid)", 
                         "MH 1541 (86M53) (Hybrid)", "RHB 177 (MH 1486)", "HHB 226 (MH 1479)"],
        "Finger Millet": ["GPU 67"],
        "Indian Mustard": ["DRMR 601 (NRCDR 601)", "Pusa Mustard 26 (NPJ-113)", "Pusa Mustard 27 (EJ-17)", 
                           "CORAL 432 (PAC 432)(Hybrid)", "Pitambari (RYSK-05-02)"],
        "Groundnut": ["Girnar - 3 (PBS 12160)", "Kadiri Harithandhra (K 1319)", "GPBD 5"],
        "Bengal Gram": ["Ujjawal (IPCK2004-29)", "PKV KABULI-4", "MNK-1"],
        "Sugarcane": ["Karan 6 (Co 0239)", "Karan 5 (Co 0124)", "Co-0218"],
        "Jute": ["SUDHANGSU (JBO-1)", "ARPITA (JBC-5)"],
        "Mesta": ["SNEHA (JRM-3)", "SHRESTHA (JRM-5)"],
        "Cotton": ["CNH012", "CICR-3 (CISA 614)", "VBCH 2231", "FDK 124"]
    };
    
    const varietySelect = document.getElementById('variety');
    varietySelect.innerHTML = '';  // Clear the current options
    
    if (crop in varieties) {
        varieties[crop].forEach(function(variety) {
            const option = document.createElement('option');
            option.value = variety;
            option.textContent = variety;
            varietySelect.appendChild(option);
        });
    }
}
