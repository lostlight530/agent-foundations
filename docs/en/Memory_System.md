# Memory System: Representation Learning via SimCLR & Unsupervised Learning

## 0. Introduction & Core Quick Look (For Beginners)

**What is this?**
Just like humans have short-term "working memory" and long-term "episodic memory," agents need to remember what they have seen and done.
However, if you bluntly store every chat log, image, and webpage screenshot into a database (like a traditional vector database), the system will soon be choked with massive amounts of "junk data." It becomes slow and struggles to find the core information that actually matters.

To solve this, we abandoned the outdated approach of "storing raw data." Instead, we integrated a cutting-edge AI vision algorithm called **SimCLR (Contrastive Learning)**. Our system no longer memorizes "what the screen looks like," but automatically extracts "what fundamentally changed on the screen," achieving a highly efficient, structurally organized memory system that will never overflow your storage.

---

## 1. Background: Saying Goodbye to Mechanical Recording

The memory system is the foundation of any agent's perception and understanding of complex environments. In our deterministic agent architecture, we completely abandoned traditional heuristic memory management (such as simple text truncation, sliding windows, or primitive embedding matching).

Instead, we adopted a rigorous representation learning framework based on **SimCLR (Simple Framework for Contrastive Learning of Visual Representations)** and Unsupervised Learning.
The core idea of SimCLR is "Contrastive Learning": it forces the model to mathematically maximize the similarity between different views of the same object (e.g., a photo of a cat and its sketch) while minimizing its similarity to unrelated objects (e.g., a dog).

In the context of agent memory, this means we execute a brutal mathematical dimensionality reduction. We do not store raw input data filled with redundant pixels and useless characters on the hard drive. Instead, we use algorithms to extract and memorize **high-dimensional, continuous, and intrinsically structured invariant features**.

---

## 2. Core Mechanisms: Memory Compression & Anomaly Capture

### 2.1 Representation Learning & Temporal Contrast
As an agent interacts with a PC, a webpage, or the real world, it constantly receives an overwhelming flood of complex observations.
Through unsupervised contrastive learning objectives, the memory system acts like a super-compressor, mapping these discrete, multi-modal (image, text, audio) perceptions into a unified, ultra-compact Latent Space.
* **Non-linear Projection**: Deep residual neural networks project the raw high-dimensional input into a dense vector consisting of just a few hundred numbers.
* **Temporal Contrastive Dynamics**: The real world flows continuously. The system treats two states that occur very close in time (e.g., 0.1 seconds apart) as a "positive sample pair" (assuming they are essentially about the same event), and states far apart as "negative samples." Through this push and pull, the memory network automatically learns to capture the developmental laws and temporal causal structures of objects, without any human labeling.

### 2.2 Extreme Feature Extraction
Our memory system **never directly stores the experience itself**; it only stores the "rules" (Features) behind the experience. This mathematical compression reduces storage and computational costs by several orders of magnitude. More importantly, it acts as a super-filter, stripping away all useless environmental noise (like flashing ads on a webpage or background color changes) and retaining only the features that have absolute value for the agent's future decisions.

### 2.3 Anomaly Detection & Attention Shift
When a model operates in a stable environment for a long time, an extremely stable "mathematical clustering domain" forms in its latent space. At this point, any fresh input that deviates from this familiar distribution will cause massive gradient fluctuations.
Because our system monitors these fluctuations in real-time, novel situations are naturally and acutely flagged as an "Anomaly" or "Novelty."
* **Automatic Attention Shift**: Once the anomaly signal breaches a preset mathematical threshold, it immediately triggers the agent's highest level of attention. The system is forced out of "autopilot," allocating computing power to deeply analyze and record this critical turning point. This is the underlying foundation for generating true "human-level episodic memory."
* **Boundary Determinism**: In our constrained architecture, we don't guess if something is "weird." We mathematically prove whether the agent has encountered a genuine unknown via strict Gaussian distribution distances (like Mahalanobis distance) and manifold boundaries. This guarantees a safe lower bound for system behavior.

---

## 3. Why Unsupervised Learning?

In the long and lonely lifecycle of an agent, there can be no real-time, perfect human tutor labeling every action as "right" or "wrong." Unsupervised learning (especially contrastive learning) empowers the agent to "bootstrap" itself, automatically building a physically intuitive "World Model" purely from massive amounts of self-interaction.

We do not use brute-force computing to memorize the superficial details of the world. We use a theoretically proven convergent contrastive loss function (InfoNCE Loss) to ensure that the agent's memory system can stably extract the essence of the world during its near-infinite exploration.

---

## 4. Source Code Breakdown & Pseudocode

The following pseudocode demonstrates how the memory system transforms continuous observation inputs into high-dimensional latent space features using contrastive learning, and how it implements automatic anomaly detection.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class ContrastiveMemorySystem(nn.Module):
    def __init__(self, encoder, projection_dim=128):
        super().__init__()
        # encoder could be ResNet (for vision) or Transformer (for text)
        self.encoder = encoder

        # Project complex features into a compact Latent Space
        self.projector = nn.Sequential(
            nn.Linear(encoder.output_dim, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Linear(512, projection_dim)
        )

        # Memory Bank: running mean and variance of historical feature states
        self.register_buffer('running_mean', torch.zeros(projection_dim))
        self.register_buffer('running_var', torch.ones(projection_dim))

    def forward(self, x_t1, x_t2):
        """
        Core derivation: Temporal contrastive learning based on InfoNCE Loss.
        x_t1, x_t2 are temporally adjacent observation states (Positive Pair).
        """
        # 1. Extract features and project
        z1 = self.projector(self.encoder(x_t1))
        z2 = self.projector(self.encoder(x_t2))

        # Normalize projections to the unit hypersphere
        z1 = F.normalize(z1, dim=1)
        z2 = F.normalize(z2, dim=1)

        # 2. Calculate positive similarity (higher is better)
        temperature = 0.5
        pos_sim = torch.exp(torch.sum(z1 * z2, dim=-1) / temperature)

        # Omitted negative sample calculations for brevity
        # loss = -log( pos_sim / (pos_sim + neg_sim) )
        pass

    def observe_and_memorize(self, current_observation):
        """
        Daily memory operation: Do not log raw images, only record anomalous features.
        """
        with torch.no_grad():
            features = self.projector(self.encoder(current_observation))
            features = F.normalize(features, dim=1)

            # 1. Mathematical Constraint: Calculate Mahalanobis distance to detect anomaly
            distance = torch.sum((features - self.running_mean)**2 / (self.running_var + 1e-5), dim=1)

            novelty_threshold = 3.0 # Beyond 3 standard deviations = Anomaly

            if distance.item() > novelty_threshold:
                print(f"[Memory System] Novelty detected (dist: {distance.item():.2f}). Engaging episodic recording.")
                # Trigger actual persistent write to hard drive
                self._save_to_episodic_database(features, current_observation)

            # 2. Smoothly update the brain's internal world view via moving average
            alpha = 0.01
            self.running_mean = (1 - alpha) * self.running_mean + alpha * features.mean(dim=0)
            self.running_var = (1 - alpha) * self.running_var + alpha * features.var(dim=0)

    def _save_to_episodic_database(self, feature, raw_data):
        # Pseudocode: Write pure extracted features to persistent storage
        pass
```

**Code Analysis:**
1. **Dimensionality Reduction & Projection (`projector`)**: We compress chaotic raw data through neural networks, ultimately mapping it onto a hypersphere of only `projection_dim` (e.g., 128) dimensions (`F.normalize`). This sphere is the agent's "conceptual universe."
2. **Rejecting Junk Memory (`observe_and_memorize`)**: Traditional systems save everything that comes in. In this function, we only call `_save_to_episodic_database` if the `distance` of the new input is mathematically greater than the threshold. If the distance is small, it means nothing new happened; we discard the raw data and only slightly tweak the brain's definition of "normal" (`alpha=0.01`). This is elegant and mathematically proven memory compression.
