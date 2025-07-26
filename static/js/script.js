
        // Create animated particles
        function createParticles() {
            const particles = document.getElementById('particles');
            const particleCount = 80;

            for (let i = 0; i < particleCount; i++) {
                const particle = document.createElement('div');
                particle.className = 'particle';
                particle.style.left = Math.random() * 100 + '%';
                particle.style.top = Math.random() * 100 + '%';
                particle.style.animationDelay = Math.random() * 8 + 's';
                particle.style.animationDuration = (Math.random() * 4 + 4) + 's';
                particles.appendChild(particle);
            }
        }

        // Scroll to form function
        function scrollToForm() {
            document.getElementById('prediction-form').scrollIntoView({
                behavior: 'smooth'
            });
        }

        // Form submission handler
        document.getElementById('predictionForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Show loading animation
            document.getElementById('loading').style.display = 'block';
            document.getElementById('results').style.display = 'none';
            
            // Get form values
            const airTemp = parseFloat(document.getElementById('airTemp').value);
            const processTemp = parseFloat(document.getElementById('processTemp').value);
            const rotSpeed = parseInt(document.getElementById('rotSpeed').value);
            const torque = parseFloat(document.getElementById('torque').value);
            const toolWear = parseInt(document.getElementById('toolWear').value);
            const typeCategory = document.getElementById('typeCategory').value;
            
            // Simulate prediction (replace with actual API call)
            setTimeout(() => {
                // Hide loading
                document.getElementById('loading').style.display = 'none';
                
                // Simple rule-based prediction for demo
                let prediction = 0;
                let riskFactors = 0;
                
                // Risk assessment based on parameters
                if (airTemp > 310 || airTemp < 295) riskFactors++;
                if (processTemp > 315 || processTemp < 305) riskFactors++;
                if (rotSpeed > 2000 || rotSpeed < 1000) riskFactors++;
                if (torque > 50 || torque < 20) riskFactors++;
                if (toolWear > 200) riskFactors++;
                if (typeCategory === 'H') riskFactors++;
                
                prediction = riskFactors > 3 ? 1 : 0;
                
                // Display results
                const resultElement = document.getElementById('predictionResult');
                const descriptionElement = document.getElementById('resultDescription');
                
                if (prediction === 1) {
                    resultElement.textContent = 'HIGH FAILURE RISK';
                    resultElement.className = 'prediction-result result-high-risk';
                    descriptionElement.textContent = 'The machine shows high probability of failure. Immediate maintenance recommended.';
                } else {
                    resultElement.textContent = 'MACHINE HEALTHY';
                    resultElement.className = 'prediction-result result-healthy';
                    descriptionElement.textContent = 'The machine is operating within normal parameters. Continue monitoring.';
                }
                
                document.getElementById('results').style.display = 'block';
                
                // Scroll to results
                document.getElementById('results').scrollIntoView({
                    behavior: 'smooth'
                });
                
            }, 2000);
        });

        // Initialize particles when page loads
        window.addEventListener('load', createParticles);

        // Add form validation styling
        document.querySelectorAll('input, select').forEach(element => {
            element.addEventListener('input', function() {
                if (this.checkValidity()) {
                    this.style.borderColor = 'rgba(46, 204, 113, 0.6)';
                    this.style.boxShadow = '0 0 10px rgba(46, 204, 113, 0.2)';
                } else {
                    this.style.borderColor = 'rgba(231, 76, 60, 0.6)';
                    this.style.boxShadow = '0 0 10px rgba(231, 76, 60, 0.2)';
                }
            });
        });

        // Add smooth scroll behavior
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });
  